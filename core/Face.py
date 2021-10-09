class Face:
  def __init__(self, id, score, boundingBox):
    self.id = id
    self.score = score
    self.boundingBox = boundingBox

  def __str__(self) -> str:
    return "Face #%d with %.1f%% at %s" % (self.id, self.score * 100, self.boundingBox)

