import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input", default="Great Wall", help="Your input for gpt prompting or dir"
    )
    parser.add_argument(
        "--read_from_file", default=False, help = "use file to read"
    )
    parser.add_argument(
        "--output_dir", default="output.txt", help = "use file to output"
    )
    parser.add_argument(
        "--api_key", default="", help="api key for gpt3.5"
    )
    parser.add_argument(
        "--need_series", default=False, help="if need series key to instruct"
    )
    parser.add_argument(
        "--series", default="series_prompt.json", help="series file path"
    )
    parsed_args = parser.parse_args()
    return parsed_args

#sk
#-P4sGP3dKgkVUWYXuadxKT3BlbkFJA5r6l0LkvduWDSGNVZnQ

args = parse_arguments()
