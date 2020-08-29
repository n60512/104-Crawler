import argparse

parser = argparse.ArgumentParser()


parser.add_argument("--output_dir", default="104-Crawler/output/", type=str, required=False,
                    help="The output directory where the .csv file will be saved.")

parser.add_argument("--key_word", default=None, type=str, required=True,
                    help="Key word for searching job.")

parser.add_argument("--min_salary", default=0, type=int,
                    help="min_salary")
parser.add_argument("--max_salary", default=9999999, type=int,
                    help="max_salary")

parser.add_argument("--max_page", default=None, type=int,
                    help="How many pages for fetch.")

parser.add_argument("--area", default=None, type=str,
                    help="Where to work.")

args = parser.parse_args()