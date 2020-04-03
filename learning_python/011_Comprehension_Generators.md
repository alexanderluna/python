# Comprehension

Python has a powerfull built in feature for working with loops called
**comprehension**. It allows us to write loops more efficiently.

```python
destinations = []
for dest in flights.values():
  destinations.append(dest.title())

# using comprehension
destinations = [ dest.title() for dest in flight.values() ]
```

The syntax looks a bit harder than a normal for loop. However, the interpreter
is optimized for comprehensions and thus executes them faster than for loops.
You are not limited to lists either. You can create dictionaries and sets as
well.

```python
# dictionary
flights = { time: destination for time, destination in flights.values() }

# set
flight_times_for_destination = {
  dest: [ time for time, destination in flight.items() if destination == dest]
  for dest in set(flight.values())
}
```

> There is no Tuple comprehension because Tuples are immutable

## Generator

It is also possible to use this syntax to generate data. They are called
generators and the result is similar to a comprehension but it operates
different. The interpreter only allocates memory for 1 item at the time. A
comprehension allocates memory for the entire list.
