# intervalgraphs.py

This repository contains a Python script that provides functionalities for graph analysis. The script utilizes Lexicographic Breadth-First Search (LexBFS) to perform various graph-related tasks.


## Table of Contents
- [Methods](#methods)
  - [LexBFS Order](#lexbfs-order)
  - [Chordality Check](#chordality-check)
  - [Interval Graph Check](#interval-graph-check)

## Methods

### LexBFS Order

This method calculates the LexBFS ordering of the nodes in the graph. LexBFS is a graph traversal algorithm that generates an ordering of nodes based on a lexicographic breadth-first search. The generated order has applications in graph theory and optimization.

### Chordality Check

Chordal graphs are graphs in which all cycles of four or more vertices have a chord, which is an edge that is not part of the cycle but connects two vertices of the cycle. This method checks if a given graph is chordal.

### Interval Graph Check

An interval graph is a type of graph that can be represented by a collection of intervals on the real line, where two intervals intersect if and only if their corresponding vertices are adjacent. This method checks if a given graph is an interval graph.
