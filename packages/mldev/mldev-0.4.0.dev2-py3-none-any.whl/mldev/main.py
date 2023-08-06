# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://gitlab.com/mlrep/mldev/-/blob/master/NOTICE.md

"""
Main module
===========

This is the entry point of the ``mldev`` command.

"""

import argparse
import os, sys
import logging

from mldev_config_parser.config_parser import MLDevSettings
from mldev.yaml_loader import YamlLoaderWithEnvVars
from mldev.utils import exec_tool_command
from mldev import logger

MSG_LOG_LEVEL = "Set logger.level in <experiment>/.mldev/config.yaml to DEBUG to see more details"


def run_experiment(experiment="./experiment.yml", pipeline="pipeline"):
    """
    Runs the pipeline from the experiment in the ``MLDEV`` environment.
    Stages and services execute in the ``EXPERIMENT`` environment (<base_folder>/venv)

    Calls ``pipeline()`` loaded from the ``experiment``. If the pipeline
    is not callable, it treats the object with name given by ``pipeline``
    as a list and passes it to ``GenericPipeline`` as ``runs``.

    Uses ``YamlLoaderWithEnvVars`` to load the experiment file.

    :param experiment: a path to experiment spec, in yaml
    :param pipeline: the name of the pipeline (top level attribute name) to call

    :returns: error_code, 0 if OK, 1 if not
    """
    try:
        from mldev.experiment import GenericPipeline

        logger.info(f"Loading {experiment}")
        config_loader = YamlLoaderWithEnvVars(experiment)
        experiment_config = config_loader.load_config()
        stages = experiment_config.get(pipeline)

        logger.info(f"Running {pipeline} from {experiment}")
        if not callable(stages):
            stages = GenericPipeline(runs=stages)

        stages(None, experiment=experiment_config, mode="prepare")
        stages(None, experiment=experiment_config, mode="run")

    except Exception as e:
        logger.debug(e, exc_info=True)
        logger.error(f"Cannot run mldev experiment. {MSG_LOG_LEVEL}", exc_info=False)
        return 1

    return 0


def init(args):
    """
    Implement `mldev init` command. Initializes the experiment.
    Runs in the ``MLDEV`` environment

    See ``mldev --help`` for more details.

    See ``init_*.sh`` scripts for exact shell commands being run.

    :param args:
    :return:
    """
    try:
        MLDevSettings().set_feature('MLDEV_NOCOMMIT', args.no_commit)

        env = {}
        if MLDevSettings().is_feature("MLDEV_NOCOMMIT"):
            env['MLDEV_NOCOMMIT'] = "True"

        folder = os.path.abspath(args.folder)

        if args.part in ['all', 'template']:
            if args.template is not None:
                exec_tool_command(f'init_template.sh "{folder}" "{args.template}"', environ=env)
            else:
                if args.reuse:
                    exec_tool_command(f'init_template.sh "{folder}"', environ=env)
                else:
                    exec_tool_command(f'init_template.sh "{folder}" -', environ=env)

        curr_dir = os.curdir
        try:
            # try reload config from the template
            # if there was a cmd line arg it will be reused
            os.chdir(f"{folder}")
            MLDevSettings.forget()

            MLDevSettings(args.config)

            if args.part in ['all', 'git']:
                no_commit = MLDevSettings().is_feature("MLDEV_NOCOMMIT")
                exec_tool_command(f"init_git.sh {0 if no_commit else 1}", environ=env)

            if args.part == 'lfs':
                exec_tool_command(f'init_lfs.sh', environ=env)

            if args.part in ['all', 'venv']:
                exec_tool_command(f'init_venv.sh .', environ=env)

            if MLDevSettings().is_extra('dvc'):
                if args.part in ['all', 'dvc']:
                    extra_package = MLDevSettings().get_extra_base('dvc')
                    exec_tool_command(f'init_dvc.sh .', extra=extra_package, environ=env)

            logger.info("Initialization has been done")

        finally:
            os.chdir(curr_dir)

    except Exception as e:
        logger.debug(e, exc_info=True)
        logger.error(f"Cannot initialize mldev experiment. {MSG_LOG_LEVEL}", exc_info=False)

        return 1

    return 0

def run(args):
    """
    Implements `mldev run` command. The command itself runs in the ``MLDEV`` environment,
    while stages and services of the experiment run in the ``EXPERIMENT`` environment.

    See ``mldev --help`` for more details.

    Calls ``run_experiment`` after checking the experiment spec and preparing the environment.

    :param args:
    :return:
    """
    MLDevSettings().set_feature('MLDEV_NOCOMMIT', args.no_commit)
    MLDevSettings().set_feature('FORCE_RUN', args.force_run)

    # this imports stages module from the .mldev folder (should be in PYTHONPATH)
    # mldev_stages = os.path.abspath("./.mldev")
    logger.debug(f"Current sys.path is {str(sys.path)}")
    # if mldev_stages not in map(os.path.abspath, sys.path):
    #     sys.path.append(mldev_stages)
    try:
        import stages
    except ModuleNotFoundError as err:
        logger.debug(err, exc_info=True)
        logger.warn(f"Custom stages are not found in sys.path. {MSG_LOG_LEVEL}", exc_info=False)

    experiment_file = "./experiment.yml"
    env_experiment_file = MLDevSettings().get_value("EXPERIMENT_FILE")
    if args.file:
        experiment_file = args.file
    elif env_experiment_file:
        experiment_file = env_experiment_file

    run_experiment(experiment=experiment_file, pipeline=args.pipeline)


def urls(args):
    """
    Implements ``mldev urls`` command. Returns urls for active services.
    Runs in the ``MLDEV`` environment.

    See ``mldev --help`` for more info

    :param args:
    :return:
    """
    try:
        exec_tool_command(f'ngrok_urls.sh')
    except Exception as e:
        logger.debug(e, exc_info=True)
        logger.error(f"Cannot get urls for mldev experiment. {MSG_LOG_LEVEL}", exc_info=False)
        return 1

    return 0


def _version(args):
    """
    Implements ``mldev version`` command.
    Runs in the ``MLDEV`` environment.

    See ``mldev --help`` for more info

    :param args:
    :return:
    """

    try:
        from mldev.version import __version__
        print(__version__)
    except Exception as e:
        logger.debug(e, exc_info=True)
        logger.error(f"Cannot get version for mldev. {MSG_LOG_LEVEL}", exc_info=False)
        return 1

    return 0


def setup_logging():
    """
    Inits logging for mldev when run as a tool

    :return:
    """
    logger.setLevel(MLDevSettings().get_value("LOG_LEVEL"))

    if MLDevSettings().logs_dir is not None:
        test_logs_path = MLDevSettings().logs_dir
        os.makedirs(test_logs_path, exist_ok=True)

        fh = logging.FileHandler(test_logs_path + "/debug.log")
        fh.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
        fh.setLevel(logging.DEBUG)

        logger.addHandler(fh)


def do_main():
    from argparse import RawTextHelpFormatter
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
    parser.add_argument("--config", type=str, help="path to config.yaml file")

    subparsers = parser.add_subparsers(help='List of commands')
    version_parser = subparsers.add_parser("version", help="Prints current version")

    init_parser = subparsers.add_parser(
        "init",
        help="Creates the directories structure, starts venv, configure dvc in the specified folder",
        formatter_class=RawTextHelpFormatter
    )
    run_parser = subparsers.add_parser(
        "run",
        help="starts mldev tool in the current folder"
    )

    urls_parser = subparsers.add_parser(
        "urls",
        help="get externally accessible urls for services"
    )

    init_parser.add_argument(
        "-p", "--part",
        type=str,
        choices=['all', 'template', 'git', 'lfs', 'venv', 'dvc'],
        help="use this to init or re-init your experiment. Where:\n"
             "'all'      means 'template', 'git', 'venv', 'dvc' (if installed)\n"
             "'template' sets up the template (see also -r switch)\n"
             "'git'      inits a local Git repository for the experiment\n"
             "'lfs'      enables storing files in git lfs for Git repository\n"
             "'venv'     configures the virtual environment (required)\n"
             "'dvc'      prepares DVC for data version control (if installed as an extra)",
        default='all'
    )

    init_parser.add_argument(
        "-t", "--template",
        type=str,
        help="you may pass preferable template to organize your project properly.\n"
              "If it is not given then template will be set to the template-default.\n"
              "(tip: see https://gitlab.com/mlrep for more information)")
    init_parser.add_argument(
        "folder",
        type=str,
        help="you must specify folder for the mldev initialization"
    )

    init_parser.add_argument(
        "-r", "--reuse",
        action="store_true",
        help="set this key if you want to reuse an existing folder with your code"
    )

    run_parser.add_argument("--no-commit", action="store_true",
                             help="Disables committing data configs to Git")
    run_parser.add_argument("-f", "--file", default="",
                             help="Specify experiment file to use")
    run_parser.add_argument("pipeline", default="pipeline", nargs='?',
                             help="Set pipeline to run from the experiment")
    run_parser.add_argument("--force-run", action="store_true", default=False,
                            help="Force running the experiment regardless of any cached intermediate results")

    init_parser.add_argument("--no-commit", action="store_true",
                             help="Disables committing data configs to Git")

    init_parser.set_defaults(func=init)
    run_parser.set_defaults(func=run)
    version_parser.set_defaults(func=_version)
    urls_parser.set_defaults(func=urls)

    args = parser.parse_args()
    if args.config:
        # pre-create MLDevSetting with the config
        MLDevSettings.forget()
        MLDevSettings(args.config)

    setup_logging()
    logger.info(f"Starting mldev in {os.path.abspath(os.curdir)}")

    if not hasattr(args, 'func') or not args.func:
        parser.print_help()
        parser.exit()

    exit_code = args.func(args)

    exit(exit_code)


if __name__ == "__main__":
    do_main()
