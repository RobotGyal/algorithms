#!python

def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    for i in range(len(items) - 1):
      if items[i] > items[i + 1]:
        return False
    return True

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list."""

    maxi= max(numbers)
    mini = min(numbers)
    count_arr = [0] * (maxi-mini + 1)
    final_arr = []

    #put num count in new array
    for i in numbers:
      count_arr[i-mini] += 1

    #store total count
    for i in range(1, maxi):
      count_arr[i-mini] += count_arr[i-mini-1]   #make current into the sum of itself and last element

    #find index of original num and put in final array
    for i in count_arr:
      for _ in range(count_arr[1]):
        final_arr.append(count_arr[0])
    return final_arr

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list