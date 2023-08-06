import timeit, sys, io, contextlib
from typing import Optional, Union, TextIO, BinaryIO


class TimeItError(Exception):
  """A custom exception used to report errors in use of Timer class"""


class TimeIt:
  prefix = ' '
  __current_nesting_level = 0

  def __init__(self, title="Elapsed time", output: Optional[Union[str, TextIO, BinaryIO]] = sys.stdout):
    self.title = title
    self.output = output
    self.owns_output = False
    self._start_time = None

    if isinstance(output, str):
      self.output = open(output, 'a+t')
      self.owns_output = True
    elif isinstance(self.output, BinaryIO):
      self.output = io.TextIOWrapper(self.output)
    elif isinstance(self.output, TextIO) or \
      isinstance(self.output, io.TextIOWrapper) or \
      self.output is None:
      pass  # already a text stream or None, so no need to do anything
    # elif 'b' in getattr(self.output, 'mode', ''):
    #   pass
    else:
       raise TypeError(f"Invalid output type: {type(self.output)}")

  def start(self):
    TimeIt.__current_nesting_level = TimeIt.__current_nesting_level + 1
    """Start a new timer"""
    if self._start_time is not None:
      raise TimeItError(f"Timer is running. Use .stop() to stop it")

    self._start_time = timeit.default_timer()

  def stop(self):
    TimeIt.__current_nesting_level = TimeIt.__current_nesting_level - 1
    """Stop the timer, and report the elapsed time"""
    if self._start_time is None:
      raise TimeItError(f"Timer is not running. Use .start() to start it")

    elapsed_time = timeit.default_timer() - self._start_time
    self._start_time = None
    prefix = TimeIt.prefix * TimeIt.__current_nesting_level
    if self.output:
      print(f"{prefix}{self.title}: {elapsed_time} seconds", file=self.output)

  def __enter__(self):
    self.start()
    return self

  def __exit__(self, type, value, traceback):
    self.stop()
    if self.owns_output:
      self.output.close()


if __name__ == "__main__":
  TimeIt.prefix = '  '
  
  # Write time elapsed information to stdout, with default title
  with TimeIt() as timer:
    # Your time-consuming code here
    for _ in range(1000000):
      pass

  # Write to stdout, nested
  with TimeIt("Total time taken"):
    from time import sleep
    for _ in range(10):
      with TimeIt("Time taken - outer"):
        for _ in range(10):
          with TimeIt("Time taken - inner"):
            sleep(0.01)


  # Append to output.txt
  with TimeIt(title="Time taken", output="output.txt") as t:
    # Your time-consuming code here
    for _ in range(1000000):
      pass

  # Write to stderr
  with TimeIt(output=sys.stderr) as t:
    # Your time-consuming code here
    for _ in range(1000000):
      pass

  # Write to an output stream that the client owns!
  with open("output.txt", 'w') as f:
    with TimeIt(output=f) as t:
      # Your time-consuming code here
      for _ in range(1000000):
        pass
