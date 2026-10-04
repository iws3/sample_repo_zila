# ML Internship (Sample Repo)

Sample repository for testing the Zigex / Zila internship workflow.

## Structure
```
beginner/        1_python, 2_ai_maths, 3_eda, 4_classical_ml   (each: day_1..day_4)
intermediate/    1_deep_learning, 2_neural_nets
advanced/        1_generative_ai, 2_agents
contributors/    <github-username>/<level>/<module>/day_N/   <- interns work here
templates/       exercise.md template
.github/         PR template, validation workflow
zila/            zila-submit prototype
grading.yml      day weights (1,1,2,4) normalised to 100
```

## Workflow
1. Supervisor accepts intern on Zigex -> intern added as contributor.
2. Zila clones the repo in the background.
3. Intern works in `contributors/<username>/<level>/<module>/day_N/`.
4. Intern runs `zila-submit`: branch (`<module>/<username>/day_<n>`), commit, push and PR are automatic.
5. GitHub emails the supervisor; `validate-pr` checks the rules.
6. Tutor reviews and marks each day out of 10.

## Scoring
Weights 1:1:2:4 (total 8) = 12.5 + 12.5 + 25 + 50 = 100.
`python scripts/normalize.py marks.csv`
