import argparse

import pandas as pd


def split_colours_into_integers(df: pd.DataFrame) -> pd.DataFrame:
    # Splits the text into a list of integers for each color:
    df = df.copy()
    for color in ["red", "blue", "green"]:
        df[color] = df.record_of_games.str.findall(rf"(\d+ {color})").apply(
            lambda x: [int(item.replace(f" {color}", "")) for item in x]
        )
    return df


def part_1(df: pd.DataFrame) -> pd.DataFrame:
    mask = (
        df.red.apply(lambda x: all([item <= 12 for item in x]))
        & df.blue.apply(lambda x: all([item <= 14 for item in x]))
        & df.green.apply(lambda x: all([item <= 13 for item in x]))
    )
    return df[mask]


def part_2(df: pd.DataFrame) -> pd.DataFrame:
    # finding the minimal set using the max element of each color
    for color in ["red", "blue", "green"]:
        df[f"max_{color}"] = df[color].apply(lambda x: max(x))
    return df


def main(args: argparse.Namespace):
    ## Part One --------------------
    data = pd.read_csv(f"{args.data_dir}/day-2-part1.csv", sep=":").assign(
        gameid=lambda x: x.gameid.str.replace("Game ", "").astype(int),
    )
    splited_data = split_colours_into_integers(data)
    # print("Full data\n")
    # print(splited_data.head())
    print("Part One --------------------")
    part1 = part_1(splited_data)
    # print("Masked data\n")
    # print(part1.head())
    print(f"Sum of ID games: {part1.gameid.sum():,}")
    print("Part Two --------------------")
    part2 = part_2(splited_data)
    part2["power_min_set"] = part2.max_red * part2.max_blue * part2.max_green
    print("Adding all minimal set powers, we have:" f" {part2.power_min_set.sum():,}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "data_dir",
        help="Directory containing data. Defaults to testdata.",
        default="testdata",
    )
    args = parser.parse_args()
    main(args)
