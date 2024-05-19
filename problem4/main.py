def count_item_and_sort(items) :
    count_dict = {}
    for item in items :
        if item not in count_dict :
            count_dict[item] = 0
        count_dict[item] += 1

    sort_key = lambda x : (
        x[1],
        x[0]
    )
    sorted_items = sorted(
        count_dict.items(),
        key=sort_key
    )
    return " ".join(f"{item}->{count}" for item, count in sorted_items)


if __name__ == "__main__":
  print(count_item_and_sort(["js", "js", "golang", "ruby", "ruby", "js", "js"]))
  # "golang->1 ruby->2 js->4"
  print(count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "A", "D", "D"]))
  # "C->1 D->2 B->3 A->4"
  print(count_item_and_sort(["football", "basketball", "tenis"]))
  # "basketball->1 football->1 tenis->1"
