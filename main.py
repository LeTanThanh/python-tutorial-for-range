if __name__ == "__main__":
  # Introduction to Python for loop statement with the range() function

  """
  for index in range(n):
    statement
  """

  for index in range(5):
    print(index)

  for index in range(5):
    print(index + 1)

  # Specifying the starting value for the sequence

  """
  range(start, stop)
  """

  for index in range(1, 6):
    print(index)

  # Specifying the increment for the sequence

  """
  range(start, stop, step)
  """

  for index in range(0, 11, 2):
    print(index)
