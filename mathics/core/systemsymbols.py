# -*- coding: utf-8 -*-
"""
Symbols for some (but not all) Mathics primitive names

We put all of this in one place to make it easy to find most of them.

There are other Symbols, such as those for True and False that are
needed in the Symbol class. So those are defined there, not here.

Other modules may also define Symbols which are thought to be
lesser-used, or is will probably only be use in the module where it is
defined. Over time, as we find more uses of these, they are sometimes
moved here.

"""


from mathics.core.symbols import Symbol

# Note that at the time this is evaluated Symbol("System`X")
# is the same as Symbol("X"), but it is better to make this
# explicit. A Pymathics module for example may decide to define
# its own Symbol X that also appears here after System`

# This list is sorted in alphabetic order.
SymbolAborted = Symbol("System`$Aborted")
SymbolAccuracy = Symbol("System`Accuracy")
SymbolAll = Symbol("System`All")
SymbolAlternatives = Symbol("System`Alternatives")
SymbolAnd = Symbol("System`And")
SymbolAppend = Symbol("System`Append")
SymbolApply = Symbol("System`Apply")
SymbolArcCos = Symbol("System`ArcCos")
SymbolArcSin = Symbol("System`ArcSin")
SymbolArcTan = Symbol("System`ArcTan")
SymbolAssociation = Symbol("System`Association")
SymbolAssumptions = Symbol("System`$Assumptions")
SymbolAttributes = Symbol("System`Attributes")
SymbolAutomatic = Symbol("System`Automatic")
SymbolBlank = Symbol("System`Blank")
SymbolBlankNullSequence = Symbol("System`BlankNullSequence")
SymbolBlankSequence = Symbol("System`BlankSequence")
SymbolBlend = Symbol("System`Blend")
SymbolBreak = Symbol("System`Break")
SymbolByteArray = Symbol("System`ByteArray")
SymbolC = Symbol("System`C")
SymbolCatalan = Symbol("System`Cases")
SymbolCatalan = Symbol("System`Catalan")
SymbolCeiling = Symbol("System`Ceiling")
SymbolClusteringComponents = Symbol("System`ClusteringComponents")
SymbolColorConvert = Symbol("System`ColorConvert")
SymbolColorData = Symbol("System`ColorData")
SymbolColorQuantize = Symbol("System`ColorQuantize")
SymbolCompile = Symbol("System`Compile")
SymbolCompiledFunction = Symbol("System`CompiledFunction")
SymbolComplex = Symbol("System`Complex")
SymbolComplexInfinity = Symbol("System`ComplexInfinity")
SymbolCondition = Symbol("System`Condition")
SymbolConditionalExpression = Symbol("System`ConditionalExpression")
SymbolConjugate = Symbol("System`Conjugate")
SymbolContainsOnly = Symbol("System`ContainsOnly")
SymbolContext = Symbol("System`$Context")
SymbolContextPath = Symbol("System`$ContextPath")
SymbolContinue = Symbol("System`Continue")
SymbolCos = Symbol("System`Cos")
SymbolCosh = Symbol("System`Cosh")
SymbolCot = Symbol("System`Cot")
SymbolCoth = Symbol("System`Coth")
SymbolCovariance = Symbol("System`Covariance")
SymbolD = Symbol("System`D")
SymbolDefault = Symbol("System`Default")
SymbolDefinition = Symbol("System`Definition")
SymbolDerivative = Symbol("System`Derivative")
SymbolDirectedInfinity = Symbol("System`DirectedInfinity")
SymbolDispatch = Symbol("System`Dispatch")
SymbolDot = Symbol("System`Dot")
SymbolDownValues = Symbol("System`DownValues")
SymbolE = Symbol("System`E")
SymbolEdgeForm = Symbol("System`EdgeForm")
SymbolEqual = Symbol("System`Equal")
SymbolEquivalent = Symbol("System`Equivalent")
SymbolEulerGamma = Symbol("System`EulerGamma")
SymbolExactNumberQ = Symbol("System`ExactNumberQ")
SymbolExpandAll = Symbol("System`ExpandAll")
SymbolExport = Symbol("System`Export")
SymbolExportString = Symbol("System`ExportString")
SymbolFaceForm = Symbol("System`FaceForm")
SymbolFactorial = Symbol("System`Factorial")
SymbolFailed = Symbol("System`$Failed")
SymbolFindClusters = Symbol("System`FindClusters")
SymbolFloor = Symbol("System`Floor")
SymbolFormat = Symbol("System`Format")
SymbolFractionBox = Symbol("System`FractionBox")
SymbolFullForm = Symbol("System`FullForm")
SymbolFunction = Symbol("System`Function")
SymbolGamma = Symbol("System`Gamma")
SymbolGet = Symbol("System`Get")
SymbolGoldenRatio = Symbol("System`GoldenRatio")
SymbolGraphics = Symbol("System`Graphics")
SymbolGraphics3D = Symbol("System`Graphics3D")
SymbolGreater = Symbol("System`Greater")
SymbolGreaterEqual = Symbol("System`GreaterEqual")
SymbolGrid = Symbol("System`Grid")
SymbolHold = Symbol("System`Hold")
SymbolHoldForm = Symbol("System`HoldForm")
SymbolHoldPattern = Symbol("System`HoldPattern")
SymbolHue = Symbol("System`Hue")
SymbolIf = Symbol("System`If")
SymbolIm = Symbol("System`Im")
SymbolImage = Symbol("System`Image")
SymbolImplies = Symbol("System`Implies")
SymbolIn = Symbol("System`In")
SymbolIndeterminate = Symbol("System`Indeterminate")
SymbolInequality = Symbol("System`Inequality")
SymbolInfinity = Symbol("System`Infinity")
SymbolInfix = Symbol("System`Infix")
SymbolInputForm = Symbol("System`InputForm")
SymbolInteger = Symbol("System`Integer")
SymbolIntegrate = Symbol("System`Integrate")
SymbolLeft = Symbol("System`Left")
SymbolLength = Symbol("System`Length")
SymbolLess = Symbol("System`Less")
SymbolLessEqual = Symbol("System`LessEqual")
SymbolKey = Symbol("System`Key")
SymbolLine = Symbol("System`Line")
SymbolLog = Symbol("System`Log")
SymbolLog10 = Symbol("System`Log10")
SymbolLogPlot = Symbol("System`LogPlot")
SymbolMachinePrecision = Symbol("System`MachinePrecision")
SymbolMakeBoxes = Symbol("System`MakeBoxes")
SymbolMap = Symbol("System`Map")
SymbolMapThread = Symbol("System`MapThread")
SymbolMatchQ = Symbol("System`MatchQ")
SymbolMatrixQ = Symbol("System`MatrixQ")
SymbolMathMLForm = Symbol("System`MathMLForm")
SymbolMatrixPower = Symbol("System`MatrixPower")
SymbolMax = Symbol("System`Max")
SymbolMaxPrecision = Symbol("System`$MaxPrecision")
SymbolMaxExtraPrecision = Symbol("System`$MaxExtraPrecision")
SymbolMean = Symbol("System`Mean")
SymbolMedian = Symbol("System`Median")
SymbolMemberQ = Symbol("System`MemberQ")
SymbolMessageName = Symbol("System`MessageName")
SymbolMessages = Symbol("System`Messages")
SymbolMinus = Symbol("System`Minus")
SymbolMissing = Symbol("System`Missing")
SymbolN = Symbol("System`N")
SymbolNIntegrate = Symbol("System`NIntegrate")
SymbolNValues = Symbol("System`NValues")
SymbolNeeds = Symbol("System`Needs")
SymbolNone = Symbol("System`None")
SymbolNorm = Symbol("System`Norm")
SymbolNormal = Symbol("System`Normal")
SymbolNot = Symbol("System`Not")
SymbolNothing = Symbol("System`Nothing")
SymbolNumberForm = Symbol("System`NumberForm")
SymbolNumberQ = Symbol("System`NumberQ")
SymbolNumericQ = Symbol("System`NumericQ")
SymbolO = Symbol("System`O")
SymbolOptionValue = Symbol("System`OptionValue")
SymbolOptional = Symbol("System`Optional")
SymbolOptions = Symbol("System`Options")
SymbolOptionsPattern = Symbol("System`OptionsPattern")
SymbolOr = Symbol("System`Or")
SymbolOut = Symbol("System`Out")
SymbolOutputForm = Symbol("System`OutputForm")
SymbolOverflow = Symbol("System`Overflow")
SymbolOwnValues = Symbol("System`OwnValues")
SymbolPackages = Symbol("System`$Packages")
SymbolPart = Symbol("System`Part")
SymbolPattern = Symbol("System`Pattern")
SymbolPatternTest = Symbol("System`PatternTest")
SymbolPi = Symbol("System`Pi")
SymbolPiecewise = Symbol("System`Piecewise")
SymbolPlot = Symbol("System`Plot")
SymbolPoint = Symbol("System`Point")
SymbolPower = Symbol("System`Power")
SymbolPolygon = Symbol("System`Polygon")
SymbolPossibleZeroQ = Symbol("System`PossibleZeroQ")
SymbolPrecision = Symbol("System`Precision")
SymbolQuantity = Symbol("System`Quantity")
SymbolQuiet = Symbol("System`Quiet")
SymbolQuotient = Symbol("System`Quotient")
SymbolQuotientRemainder = Symbol("System`QuotientRemainder")
SymbolRGBColor = Symbol("System`RGBColor")
SymbolRandomComplex = Symbol("System`RandomComplex")
SymbolRandomReal = Symbol("System`RandomReal")
SymbolRational = Symbol("System`Rational")
SymbolRe = Symbol("System`Re")
SymbolReal = Symbol("System`Real")
SymbolRealDigits = Symbol("System`RealDigits")
SymbolRepeated = Symbol("System`Repeated")
SymbolRepeatedNull = Symbol("System`RepeatedNull")
SymbolReturn = Symbol("System`Return")
SymbolReverse = Symbol("System`Reverse")
SymbolRight = Symbol("System`Right")
SymbolRound = Symbol("System`Round")
SymbolRow = Symbol("System`Row")
SymbolRowBox = Symbol("System`RowBox")
SymbolRule = Symbol("System`Rule")
SymbolRuleDelayed = Symbol("System`RuleDelayed")
SymbolSameQ = Symbol("System`SameQ")
SymbolSequence = Symbol("System`Sequence")
SymbolSeries = Symbol("System`Series")
SymbolSeriesData = Symbol("System`SeriesData")
SymbolSet = Symbol("System`Set")
SymbolSign = Symbol("System`Sign")
SymbolSimplify = Symbol("System`Simplify")
SymbolSin = Symbol("System`Sin")
SymbolSinh = Symbol("System`Sinh")
SymbolSlot = Symbol("System`Slot")
SymbolSparseArray = Symbol("System`SparseArray")
SymbolSplit = Symbol("System`Split")
SymbolSqrt = Symbol("System'Sqrt")
SymbolSqrtBox = Symbol("System`SqrtBox")
SymbolStandardDeviation = Symbol("System`StandardDeviation")
SymbolStandardForm = Symbol("System`StandardForm")
SymbolStringForm = Symbol("System`StringForm")
SymbolStringInsert = Symbol("System`StringInsert")
SymbolStringJoin = Symbol("System`StringJoin")
SymbolStringPosition = Symbol("System`StringPosition")
SymbolStringQ = Symbol("System`StringQ")
SymbolStringRiffle = Symbol("System`StringRiffle")
SymbolStringSplit = Symbol("System`StringSplit")
SymbolStyle = Symbol("System`Style")
SymbolSubValues = Symbol("System`SubValues")
SymbolSubsetQ = Symbol("System`SubsetQ")
SymbolSubtract = Symbol("System`Subtract")
SymbolSubscriptBox = Symbol("System`SubscriptBox")
SymbolSubsuperscriptBox = Symbol("System`SubsuperscriptBox")
SymbolSuperscriptBox = Symbol("System`SuperscriptBox")
SymbolTable = Symbol("System`Table")
SymbolTan = Symbol("System`Tan")
SymbolTanh = Symbol("System`Tanh")
SymbolTeXForm = Symbol("System`TeXForm")
SymbolThrow = Symbol("System`Throw")
SymbolThreshold = Symbol("System`Threshold")
SymbolToString = Symbol("System`ToString")
SymbolTotal = Symbol("System`Total")
SymbolTraditionalForm = Symbol("System`TraditionalForm")
SymbolUndefined = Symbol("System`Undefined")
SymbolUnequal = Symbol("System`Unequal")
SymbolUnevaluated = Symbol("System`Unevaluated")
SymbolUpValues = Symbol("System`UpValues")
SymbolVariance = Symbol("System`Variance")
SymbolXor = Symbol("System`Xor")
