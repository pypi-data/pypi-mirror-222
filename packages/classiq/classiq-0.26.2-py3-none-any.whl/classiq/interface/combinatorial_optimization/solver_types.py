import enum


class QSolver(str, enum.Enum):
    QAOAPenalty = "QAOAPenalty"
    QAOAMixer = "QAOAMixer"
    Custom = "Custom"
    GAS = "GAS"
