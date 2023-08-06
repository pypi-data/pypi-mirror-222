#!/usr/bin/python3
import argparse
from dacite import from_dict
from gitlab_ps_utils.api import GitLabApi
from gitlab_evaluate.migration_readiness.report_generator import ReportGenerator
from gitlab_evaluate.lib import api as evaluate_api
from gitlab_evaluate.lib.api_models.application_stats import GitLabApplicationStats
import logging

def main():
    logging.basicConfig(filename='evaluate.log', level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--token", help="Personal Access Token: REQ'd")
    parser.add_argument("-s", "--source", help="Source URL: REQ'd")
    parser.add_argument(
        "-f", "--filename", help="CSV Output File Name. If not set, will default to 'evaluate_output.csv'")
    parser.add_argument("-o", "--output", action='store_true',
                        help="Output Per Project Stats to screen")
    parser.add_argument("-i", "--insecure", action='store_true',
                        help="Set to ignore SSL warnings.")
    parser.add_argument(
        "-p", "--processes", help="Number of processes. Defaults to number of CPU cores")
    parser.add_argument(
        "-g", "--group", help="Group ID. Evaluate all group projects (including sub-groups)")

    args = parser.parse_args()

    if None not in (args.token, args.source):
        processes = args.processes if args.processes else None


        source = args.source

        if args.insecure:
            gitlabApi = GitLabApi(ssl_verify=False)
        else:
            gitlabApi = GitLabApi()

        evaluateApi = evaluate_api.EvaluateApi(gitlabApi)

        rg = ReportGenerator(source, args.token, filename=args.filename,
                             output_to_screen=args.output, evaluate_api=evaluateApi, processes=processes)

        rg.get_app_stats(source, args.token)
        rg.handle_getting_data(args.group)
        rg.handle_getting_user_data(args.group)
        rg.write_workbook()

    else:
        parser.print_help()
