Optimization
Module 1: Foundations
Om Prakash
```
iPrana (Intelligent Process Analytics Lab)
```
Department of Chemical Engineering
Indian Institute of Technology Delhi
New Delhi, India-110016
```
Email: omprakash@iitd.ac.in
```
```
Web: https://iprana-lab.github.io
```
December 26, 2025
Optimization is everywhere! – An ubiquitous problem Ô
Scopus search1:
26,33,115 documents found
2,27,411 documents in 2024
1Data till 2024
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) December 26, 2025 1 / 34
```
Optimization is everywhere! – An ubiquitous problem Ô
Sometimes, there are conflicting goals.
But that is life ⌣
– Find trade-off point
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) December 26, 2025 2 / 34
```
Optimization is everywhere! – An ubiquitous problem Ô
Sometimes, there are conflicting goals.
But that is life ⌣
– Find trade-off point
infeasible solution
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) December 26, 2025 2 / 34
```
```
Optimization: A core È foundation of Machine Learning
```
```
1Deisenroth, M. P., Faisal, A. A., & Ong, C. S. (2020). Mathematics for machine learning. Cambridge University Press.
```
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) December 26, 2025 3 / 34
```
What is Optimization - layman?
Finding the best way to complete a task, given the available resources.
```
Task: Book car(s) and
```
```
fit the luggage;
```
```
Constraints: Money
```
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) December 26, 2025 4 / 34
```
What is Optimization - layman?
Finding the best way to complete a task, given the available resources.
```
Task: Book car(s) and
```
```
fit the luggage;
```
```
Constraints: Money
```
```
Task: Fit max boxes
```
```
in one go;
```
```
Constraints: Two
```
hands, shoulders and
legs
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) December 26, 2025 4 / 34
```
What is Optimization - layman?
Finding the best way to complete a task, given the available resources.
```
Task: Book car(s) and
```
```
fit the luggage;
```
```
Constraints: Money
```
```
Task: Fit max boxes
```
```
in one go;
```
```
Constraints: Two
```
hands, shoulders and
legs
```
Task: Dry your hands;
```
```
Unconstrained: Unlimited resource Or,
```
```
Constraints: Limited resource
```
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) December 26, 2025 4 / 34
```
What is Optimization?
Finding the best way to complete a task.
▶ Defining task is the most important problem
▶ There may be constraints
Essential features of optimization
1 Objective function
2 Equality constraint
3 Inequality constraint
Unconstrained optimization:
```
Minimizex f (x)
```
```
f (x) is a scalar function: Objective function
```
x is the vector of decision variables whose
value needs to be set
Constrained optimization:
```
Minimizex f (x)
```
```
such that, h(x) = 0 [Equality constraint]
```
```
g(x) ≥ 0 [Inequality constraint]
```
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) December 26, 2025 5 / 34
```
```
1Deisenroth, M. P., Faisal, A. A., & Ong, C. S. (2020). Mathematics for machine learning. Cambridge University Press.
```
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) December 26, 2025 6 / 34
```
Connecting dots ...
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) December 26, 2025 7 / 34
```
Connecting dots ...
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) December 26, 2025 8 / 34
```
Connecting dots ...
```
Objective function/loss: f (w, b) = (y − ˆy)2
```
```
Minimize objective function f (w, b) to obtain w and b.
```
```
minw,b f (w, b)
```
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) December 26, 2025 9 / 34
```
Connecting dots ...
```
Design of experiments (DOE) from an Optimization angle
```
E.g., Problem: 2 factors varied in 3 levels.
Proposed model: y = b0 + b1x1 + b2x2 + ϵ
▶ DOF: 3
```
▶ 9!3!(9−3)! = 84 ways to select 3 set
```
of experiments out of 9.
Say, x1 = 1, x2 = 0 is technically
infeasible.
```
Solve:
```
Maximize <Information content>,
```
such that, x1̸ = 1, x2̸ = 0, x1, x2 = {−1, 0, 1}
```
and 3 locations.
1https://www.youtube.com/watch?v=Zs5zvOv_XrI
2https://en.wikipedia.org/wiki/Optimal_experimental_design
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) December 26, 2025 10 / 34
```
```
Linear Programming (LP) formulation
```
minx c⊤x
s.t., Aeq x = beq
Ain x ≤ bin
x ∈ Rn
Optimal solution at one of the corner points.
```
Minimize f (x) = 3x + 2y
```
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 11 / 34
```
```
Nonlinear Programming (NLP) formulation
```
```
minx f (x)
```
```
s.t., h(x) = 0
```
```
g(x) ≤ 0
```
x ∈ Rn
```
Minimize f (x, y) = sin(x) cos(y) + 0.1(x2 + y2)
```
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 12 / 34
```
Combinatorial problem
1https://en.wikipedia.org/wiki/Karp’s 21 NP-complete problems
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 13 / 34
```
Combinatorial problem
Finite feasible space, but often exponential in size
Integrality requirements need to be enforced – a tough problem
Network optimization, supply chain, scheduling problem, graph theory related
problems, e.g., shortest path, minimum vertex cover, graph coloring problem, etc.
1https://en.wikipedia.org/wiki/Karp’s 21 NP-complete problems
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 13 / 34
```
```
Mixed Integer Nonlinear Programming (MINLP) formulation
```
```
minx f (x, y)
```
```
s.t., h(x, y) = 0
```
```
g(x, y) ≤ 0
```
x ∈ Zn, y ∈ Rm
```
Minimize f (x, y) = sin(x) cos(y) + 0.1(x2 + y2)
```
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 14 / 34
```
Stochastic programming
“Uncertainty is the only certainty there is, and knowing how to live with insecurity is the only security.”– John Allen Paulos.
Interface of probability and optimization
▶ Existence of random parameters in the optimization problem
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 15 / 34
```
Stochastic programming
“Uncertainty is the only certainty there is, and knowing how to live with insecurity is the only security.”– John Allen Paulos.
Interface of probability and optimization
▶ Existence of random parameters in the optimization problem
```
Objective function: minx EFα [h(x, α)]
```
```
Data driven optimization techniques (ML) used to solve
```
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 15 / 34
```
Stochastic programming
“Uncertainty is the only certainty there is, and knowing how to live with insecurity is the only security.”– John Allen Paulos.
Interface of probability and optimization
▶ Existence of random parameters in the optimization problem
```
Objective function: minx EFα [h(x, α)]
```
```
Data driven optimization techniques (ML) used to solve
```
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 15 / 34
```
Multi-objective optimization formulation
“Jack of all trades, master of none, but oftentimes better than master of one”
```
minx (f1(x), f2(x), . . . , fk(x)), k ≥ 2
```
```
s.t., h(x) = 0
```
```
g(x) ≤ 0
```
x ∈ X
Pareto-optimal set: Best tradeoff
between competing objectives.
1https://en.wikipedia.org/wiki/Multi-objective optimization
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 16 / 34
```
Types of optimization problems: Mathematical characterization
1 Unconstrained
2 Constrained
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 17 / 34
```
Types of optimization problems: Mathematical characterization
1 Unconstrained
2 Constrained
1 Linear programming
2 Non linear programming
3 Combinatorial optimization: Integer programming
4 Stochastic optimization
5 Single or multi-objective optimization
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 17 / 34
```
Optimization at many levels - Process industry perspective
Management
▶ Profitability, sustainability, safety,
investment, market strategy, supply chain
▶ Qualitative or has a high degree of
uncertainty
Design, operation, scheduling
▶ Type of equipments
▶ Size and configuration
▶ Nominal operating conditions
▶ Allocation of raw materials on a daily or
weekly basis
Individual equipment
▶ Heat exchanger efficiency, reactor yields
▶ Instrument tuning
▶ Equipment availability, fouling
management, downtime minimization1
```
Edgar, T. F., Himmelblau, D. M., & Lasdon, L. S. (2001). Optimization of chemical processes. McGraw-HillOm Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 18 / 34
```
Applications of Optimization
Determining the best plant locations, sensor placement, equipment types.
Routing tankers for the distribution of crude oil.
Sizing and layout of a pipeline.
Designing equipment and an entire plant.
Scheduling maintenance and equipment replacement.
Evaluating plant data to construct a model of a process.
Allocating resources or services among several processes.
Supply chain, planning and scheduling
```
1Edgar, T. F., Himmelblau, D. M., & Lasdon, L. S. (2001). Optimization of chemical processes. McGraw-Hill
```
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 19 / 34
```
```
Application: Real time optimization in process industry
```
Level 5: Planning & Scheduling
```
▶ Enterprise Resource Planning (ERP)
```
▶ Sets production goals subject to supply, market, and
logistics constraints
```
Level 4: Real-Time Optimization (Supervisory control)
```
▶ Provides optimal set points for each unit
▶ Adjusts for changing feedstock, utility prices,
product demands etc.
Level 3a: Regulatory Control
▶ Feedback controllers
▶ Ensures stability, handles disturbances
Level 3b: Multivariable & Constraint Control
▶ MPC handling multiple ip/op, constraints actively
▶ Ensures stability, handles disturbances
Level 2 & Level 1: Safety & Actuation
▶ Environmental constraints, equipment protection
```
systems, Measurements aSeborg, et al. Process dynamics and controlOm Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 20 / 34
```
Application of optimization
Transportation and logistics
```
▶ Dynamic vehicle routing (e.g., by Swiggy, Google Map)
```
Zhang et al., 2023, Eur. J. Oper. Res.
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 21 / 34
```
Application of optimization
Transportation and logistics
```
▶ Dynamic vehicle routing (e.g., by Swiggy, Google Map)
```
Optimization in Aerospace industry
▶ Aircraft routing
▶ Crew pairing
▶ Mitigating delays
▶ Target tracking
▶ Aerodynamic design optimization
Rail industry
Zhang et al., 2023, Eur. J. Oper. Res.
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 21 / 34
```
Application of optimization
Transportation and logistics
```
▶ Dynamic vehicle routing (e.g., by Swiggy, Google Map)
```
Optimization in Aerospace industry
▶ Aircraft routing
▶ Crew pairing
▶ Mitigating delays
▶ Target tracking
▶ Aerodynamic design optimization
Rail industry
Power systems
▶ Microgrid optimization
▶ Supply, energy trading
Nuclear engineering
Zhang et al., 2023, Eur. J. Oper. Res.
Hoummadi et al., 2025, Sci. Reports
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 21 / 34
```
Application of optimization
Transportation and logistics
```
▶ Dynamic vehicle routing (e.g., by Swiggy, Google Map)
```
Optimization in Aerospace industry
▶ Aircraft routing
▶ Crew pairing
▶ Mitigating delays
▶ Target tracking
▶ Aerodynamic design optimization
Rail industry
Power systems
▶ Microgrid optimization
▶ Supply, energy trading
Nuclear engineering
Computational biology
Agriculture
Zhang et al., 2023, Eur. J. Oper. Res.
Hoummadi et al., 2025, Sci. Reports
Schneider et al., 2019, Nature Rev. Drug
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 21 / 34
```
Common approaches and solvers for optimization problems
Problem
Type
Common Approaches Python Solvers MATLAB Solvers
LP Simplex, Interior-Point, Cutting
Planes
scipy.optimize.linprog,
PuLP, cvxpy, gurobi,
cplex
linprog
NLP Gradient Descent, Newton’s
Method, SQP, Interior-Point
scipy.optimize.minimize,
pyomo, nlopt
fmincon, fminunc
MINLP Branch-and-Bound, Outer Ap-
proximation, Decomposition
```
pyomo (Bonmin, Couenne),
```
gurobi, cplex
```
intlinprog (linear),
```
external solvers for
MINLP
SO Sample Average Approximation,
Stochastic Gradient, Robust Op-
timization
```
pyomo (stochastic), cvxpy,
```
nevergrad
Simulink toolboxes,
custom + fmincon
MOOP Weighted Sum, ϵ-Constraint,
Evolutionary Algorithms
```
(NSGA-II)
```
platypus, pymoo, deap gamultiobj,
paretosearch
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 22 / 34
```
Optimization modeling languages
General purpose Algebraic Modeling Languages
```
▶ AMPL (A Mathematical Programming Language)
```
```
▶ GAMS (General Algebraic Modeling System)
```
▶ AIMMS
```
▶ OPL (Optimization Programming Language,
```
```
part of IBM ILOG CPLEX)
```
Open source
```
▶ Pyomo (Python Optimization Modeling Objects)
```
```
▶ JuMP (Julia for Mathematical Programming)
```
▶ PuLP
▶ CVXPY
```
1 # AMPL2 # decision variables ( x [1] , x [2]) , >=0
```
```
3 var x {1..2} >= 0;4
```
5 # objective function : maximize 2* x1 + 3* x26 maximize OBJ :
```
7 2 * x [1] + 3 * x [2];8
```
9 # constraint on x [1] and x [2]10 subject to Constraint1 :
```
11 3 * x [1] + 4 * x [2] >= 1;
```
1 # Pyomo Python2 import pyomo . environ as pyo
```
34 model = pyo . ConcreteModel ()
```
```
56 # decision variables ( x [1] , x [2]) , >=0
```
```
7 model . x = pyo . Var ([1 ,2] , domain = pyo .NonNegativeReals )
```
89 # objective function : maximize 2* x1 + 3* x2
```
10 model . OBJ = pyo . Objective ( expr = 2* model . x [1]+ 3* model . x [2] , sense = pyo . maximize )
```
1112 # constraint on x [1] and x [2]
```
13 model . Constraint1 = pyo . Constraint ( expr = 3*model . x [1] + 4* model . x [2] >= 1)
```
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 23 / 34
```
Opportunities and Challenges
Optimization offers rich research opportunities and is widely applied in industry.
Challenges
▶ Scalability & Big Data
```
• Real-world problems with millions (or billions) of variables – e.g., logistics
```
▶ Nonconvex & Hard Problems
• Many real-world problems are NP-hard – e.g., protein folding
▶ Optimization under Uncertainty
• Stochastic and online optimization methods are in high demand – e.g., power distribution
▶ Real-Time & Dynamic Optimization
• Decision required in fractions of a second – e.g., self driving car
▶ Integration with Machine Learning & AI
• Optimization is the “engine” of AI/ML
▶ Multi-Objective Optimization
• Trade-offs between cost, performance, energy, and sustainability – e.g., climate modeling
▶ Sustainability & Green Optimization
• Optimizing energy systems, supply chains for low carbon footprint.
▶ Explainability & Trust
• Solutions must be interpretable, and ethical – e.g., in healthcare, nuclear engineering
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 24 / 34
```
Optimization behind ChatGPT
ChatGPT is essentially a massive optimization pipeline
Based on “transformer” neural networks.
```
Training: minimize the loss function
```
▶ e.g., cross-entropy between predicted and actual next
token
Why Optimization is central?
```
▶ Trillion of parameters updated (GPT-4)
```
▶ Requires scalable algorithms
```
▶ Constraint handling (e.g., regularization, gradient
```
```
clipping)
```
Reinforcement Learning from human feedback m l
Inference
▶ Choose a sequence of tokens – both highly likelihood
- diverse/interesting.
1https://deepsense.ai/blog/using-reinforcement-learning-to-improve-large-language-models/
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 25 / 34
```
“Optimization is in our DNA – a near-perfect design shaped by
millions of years of evolution, and still an ongoing process”
Just like Mother Nature, we can optimize continuously – learning, adapting, and improving.
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 6, 2026 26 / 34
```
```
Optimal Scheduling (Example 1.5, Edgar and Himmelblau, 1989)
```
The problem is to schedule the production in two plants, A and B, each of which can manufacture
two products, no. 1 and no. 2. How should the scheduling take place to maximize profits
while meeting the market requirements based on the data in the Table.
```
How many days per year (365 days) should each plant operate processing each kind of material?
```
1. 92.4 kg/hr
2. 94.3 kg/hr
3. 93.8 kg/hr
1. 11.1 kg/hr
2. 10.8 kg/hr
3. 11.4 kg/hr
```
(Example 1.6, Edgar and Himmelblau, 1989)
```
Suppose the flow rates entering and leaving a process are measured periodically.
Determine the best value for stream A in kg/h from the 3 hourly measurements
indicated by B and C, assuming steady-state operation at a fixed operating point.
The process model is
TA allocation in Academic setting
A department offers multiple courses in a semester. Each course requires a certain number of TA
```
hours depending on enrollment and course type (lab/theory).
```
A pool of undergraduate/graduate students are available as TAs, each with limited availability, expertise,
and eligibility constraints.
```
Goal: Allocate TAs to courses such that course requirements are met while
```
respecting student constraints and optimizing overall quality and fairness.
A chemical company can run one of the three modes to produce cheese product:
```
(i) Batch, (ii) Fed-batch, (iii) Continuous.
```
Yield, operating cost, and environmental impact differ. The production engineer must choose
exactly one mode and production rate c. Demand for the product is not fixed,
though there is an upper bound on the production rate.
Formulate an optimization problem to determine the optimal processing route
```
(only one reactor is allowed) and the optimal production rate.
```
Steps to solve optimization problems
1 Define variables
▶ Identify decision variables, parameters, and quantities of
interest
2 Set the objective/goal
▶ Choose a performance/evaluation/economic criterion
3 Build the model
```
▶ Express process relations as equations/inequalities (mass,
```
```
energy balances, empirical laws, constraints)
```
4 Simplify if needed
▶ Break into subproblems or approximate to keep tractable
5 Choose method & solve
```
▶ Select suitable technique (LP, NLP, MILP, stochastic, etc.)
```
6 Validate & analyze
▶ Check feasibility, realism, and sensitivity of solution
III
Formulation is often
the hardest part.
Domain knowledge is
essential.
There is no single recipe
– optimization is as
much art as science.
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 11, 2026 28 / 34
```
Optimization basics: Minimizers
```
Consider unconstrained optimization problem: minx∈Rnf (x)
```
```
Global minimizer: x∗ is global minimizer if f (x∗) ≤ f (x), ∀x ∈ Rn
```
▶ Finding global minimizer is difficult as our knowledge of f is usually local.
Weak local minimizer: x∗ is weak local minimizer if there is a neighbourhood
```
N (x∗), such that,
```
```
f (x∗) ≤ f (x), ∀x ∈ N (x∗)
```
```
N (x∗): an open set that contains x∗. e.g., N (x∗) = {x| ||x − x∗|| < ϵ, ∃ ϵ > 0}
```
Strong local minimizer: x∗ is strong local minimizer if there is a neighbourhood
```
N (x∗), such that,
```
```
f (x∗) < f (x), ∀x ∈ N (x∗), x̸ = x∗
```
```
Example:
```
```
▶ f (x) = 2. Every x is a weak local minimizer.
```
```
▶ f (x) = (x − 5)2. x = 5 is a strong local minimizer.
```
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 11, 2026 29 / 34
```
Optimization basics: Modality
```
Unimodal function f (x) has a strict local minimizer in the domain of interest. e.g., f (x) = (x − 5)2
```
```
Multimodal function has multiple strict local minimizer (peaks/valleys) in the domain of interest.
```
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 11, 2026 30 / 34
```
Calculus basics
Gradient
Hessian
Chain-rule
Directional derivative
Positive/negative definiteness
Taylor series https://math.libretexts.org/Bookshelves/Calculus/
```
Supplemental_Modules_(Calculus)/Multivariable_Calculus/3%3A_Topics_in_
```
Partial_Derivatives/Taylor__Polynomials_of_Functions_of_Two_Variables
Convex set, convex function
```
1Check book (Chapter 4): Optimization of Chemical Processes Himmelblau edgar
```
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 11, 2026 31 / 34
```
Gradient
Gradient of a multivariate scalar function: f : Rn → R
x ∈ Rn is a vector
```
∇f (x) =
```




∂f
∂x1∂f
∂x2
...
∂f
∂xn




```
where ∂f∂xi = limϵ→0f (x+ϵei)−f (x)ϵ , ei =
```







0
...
0
1
0
...
0







```
(1 is at the ith location)
```
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 11, 2026 32 / 34
```
Jacobian
Jacobian of a multivariate vector function: f : Rn → Rm
x ∈ Rn and f ∈ Rm are vectors
```
∇f (x) =
```
h ∂f
∂x1 . . .
∂f
∂xn
i
=


∇⊤f1
...
∇⊤fm

 =




∂f1
∂x1 . . .
∂f1
∂xn∂f2
∂x1 . . .
∂f2
∂xn
... . . . ...
∂fm
∂x1 . . .
∂fm
∂xn




∈ Rm×n
Jacobian matrix is a linear transformation with respect to infinitesimal changes
▶ Approximates a “nonlinear transformation” in a small region as a “linear
transformation”1
1https://angeloyeo.github.io/2020/07/24/Jacobian en.html
```
Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 11, 2026 33 / 34
```
Hessian
Hessian of a multivariate, scalar function f : Rn → R is the matrix of second partial
derivatives.
```
∇2f (x) =
```




∂2f
∂x21
∂2f
∂x1∂x2 . . .
∂2f
∂x1∂xn
∂2f
∂x2∂x1
∂2f
∂x22. . .
∂2f
∂x2∂xn
... ... . . . ...
∂2f
∂xn∂x1
∂2f
∂xn∂x2 . . .
∂2f
∂x2n



∈ R
n×n
```
If the second-order derivatives of f are continuous, the Hessian matrix ∇2f (x) is a
```
symmetric matrix.2
▶ i.e., function is twice continuously differentiable
2https://angeloyeo.github.io/2020/06/17/Hessian en.html
##### Om Prakash (IIT Delhi) Optimization (CLL782 / CHL7204) January 11, 2026 34 / 34