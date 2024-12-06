"""Advent of Code Day 1."""

import argparse

import number2word as n2w
import pandas as pd
import regex as re


def part_1(data: pd.DataFrame, column_to_use: str = "potential_calibration") -> int:
    data["calibration"] = (
        data[column_to_use]
        .str.findall("\d")
        .apply(lambda x: f"{x[0]}{x[-1]}")
        .astype(int)
    )
    return data.calibration.sum()


def part_2(data: pd.DataFrame) -> int:
    # local dictionary of words to numbers
    words_to_number = {n2w.convert(i).lower().strip(): i for i in range(1, 10)}
    words_to_number["sevenine"] = 79
    words_to_number["eightwo"] = 82
    words_to_number["eighthree"] = 83
    words_to_number["oneight"] = 18
    words_to_number["twone"] = 21
    words_to_number["nineight"] = 98

    data["potential_calibration_modified"] = data.potential_calibration.apply(
        lambda x: "".join(
            str(words_to_number[group]) if group in words_to_number else group
            for group in re.split(
                (
                    r"(sevenine|eightwo|oneight|twone|nineight|eighthree|"
                    r"one|two|three|four|five|six|seven|eight|nine)"
                ),
                x,
            )
        )
    )
    return part_1(data, "potential_calibration_modified")


def main(args: argparse.Namespace):
    ## Part One --------------------
    data = pd.read_csv(f"{args.data_dir}/day-1-part1.csv")
    total_calibration = part_1(data)
    print(f"\nPart One: Total calibration: {total_calibration:,}\n")

    ## Part Two --------------------
    data = pd.read_csv(f"{args.data_dir}/day-1-part2.csv")
    total_calibration = part_2(data)
    print(f"Part Two: Total calibration: {total_calibration:,}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "data_dir",
        help="Directory containing data. Defaults to testdata.",
        default="testdata",
    )
    args = parser.parse_args()
    main(args)
