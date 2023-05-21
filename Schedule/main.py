from ortools.sat.python import cp_model

num_window_workers = 3
num_shifts = 15
num_days = 30
all_workers = range(num_window_workers)
all_shifts = range(num_shifts)
all_days = range(num_days)

model = cp_model.CpModel()

shifts = {}
for n in all_workers:
    for d in all_days:
        for s in all_shifts:
            shifts[(n,d,s)] = model.NewBoolVar('shift_n%id%is%i' % (n,d,s))

for d in all_days:
    for s in all_shifts:
        model.AddExactlyOne(shifts[(n,d,s)] for n in all_workers)

for n in all_workers:
    for d in all_days:
        model.AddAtMostOne(shifts[(n, d, s)] for s in all_shifts)