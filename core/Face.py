class Face:
  def __init__(self, _id, score, bounding_box):
    self._id = _id
    self.score = score
    self.bounding_box = bounding_box

  def __str__(self) -> str:
    return "Face #%d with %.1f%% at %s" % (self._id, self.score * 100, self.bounding_box)

