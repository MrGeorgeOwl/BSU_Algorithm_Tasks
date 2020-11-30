package main

import (
	"fmt"
	"log"
)

// DepthFirstSearch finds components of graph
func DepthFirstSearch(nodes [][]int) [][]int {
	used := make([]bool, len(nodes))
	comps := make([][]int, 1)
	comps[0] = make([]int, 0)

SearchingLoop:
	for {
		indexToStartSearch := 0
		if len(used) != 0 {
			indexToStartSearch = findFirstUnusedIndex(used)
		}
		if indexToStartSearch == -1 {
			break SearchingLoop
		}
		recursiveFirstSearch(indexToStartSearch, nodes, used, comps)
		if getAmountOfUsedNodes(used) != len(nodes) {
			comps = append(comps, make([]int, 0))
		}
	}

	return comps
}

// findFirstUnusedIndex will return index of first element
// that has value of true else -1
func findFirstUnusedIndex(used []bool) int {
	for i, v := range used {
		if !v {
			return i
		}
	}
	return -1
}

// recursiveFirstSearch will go through nodes, mark them and
// recursively do the same for its neighbours
func recursiveFirstSearch(index int, nodes [][]int, used []bool, comps [][]int) {
	if used[index] {
		return
	}

	used[index] = true
	comps[len(comps) - 1] = append(comps[len(comps) - 1], index)

	for _, v := range nodes[index] {
		recursiveFirstSearch(v, nodes, used, comps)
	}
}

// getAmountOfUsedNodes return amount of true elements in slice
func getAmountOfUsedNodes(used []bool) int {
	amountOfUsedNodes := 0
	for _, v := range used {
		if v {
			amountOfUsedNodes++
		}
	}
	return amountOfUsedNodes
}

// Edge is a struct of edge in graph
type Edge struct {
	source int
	dest int
}

// EulerError error for case when euler cycle cant be build
type EulerError struct {}

func (e *EulerError) Error() string {
	return fmt.Sprintf("Euler cycle cant be build\n")
}

// FindEulerCycle will return slice of indexes
// which represents Euler cycle
func FindEulerCycle(nodes [][]int) ([]int, error) {
	if !IsEuler(nodes) {
		return nil, &EulerError{}
	}
	cycle := make([]int, 0)
	way := make([]int, 0)
	curr := 0

	for {
		// if current node dont have free edges then go back to previous node
		if len(nodes[curr]) == 0 && freeEdgesExists(nodes) {
			for len(nodes[curr]) == 0 {
				cycle = append(cycle, curr)
				curr = way[len(way) - 2]
				way = way[:len(way) - 1]
			}
		}
		// check if there any edge left
		if !freeEdgesExists(nodes) {
			break
		}
		// adding node to way and deleting edge from graph
		edge := Edge{curr, nodes[curr][0]}
		way = append(way, curr)
		curr = nodes[curr][0]
		removeEdgeFromGraph(nodes, edge)
	}
	for i := len(way) - 1; i >= 0; i-- {
		cycle = append(cycle, way[i])
	}
	return cycle, nil
}

func freeEdgesExists(nodes [][]int) bool {
	nodesWithDest := make([][]int, 0)

	for _, node := range nodes {
		if len(node) != 0 {
			nodesWithDest = append(nodesWithDest, node)
		}
	}

	return len(nodesWithDest) > 0
}

func removeEdgeFromGraph(nodes [][]int, edge Edge) {
	node := nodes[edge.source]
	if len(node) == 1 {
		node = []int{}
	} else {
		node = node[1:]
	}
	nodes[edge.source] = node
	if index := Find(nodes[edge.dest], edge.source); index != -1 {
		nodes[edge.dest] = append(nodes[edge.dest][:index], nodes[edge.dest][index + 1:]...)
	}
}

// Find index of node in nodes slice
func Find(node []int, index int) int {
	for i, v := range node {
		if v == index {
			return i
		}
	}
	return -1
}

// IsEuler returns true if Euler cycle can be found in graph
func IsEuler(nodes [][]int) bool {
	for _, v := range nodes {
		if len(v) % 2 != 0 {
			return false
		}
	}
	return true
}

func main() {
	nodes := [][]int {
		{1, 2},
		{0, 2},
		{0, 1},
		{4},
		{3},
		{6, 7, 8},
		{5, 8},
		{5, 8},
		{5, 6, 7}}
	comps := DepthFirstSearch(nodes)
	fmt.Println(comps)

	nodes = [][]int {
		{1, 4},
		{0, 2, 3, 5},
		{1, 3, 4, 5},
		{2, 1, 5, 4},
		{3, 2, 5, 0},
		{1, 2, 3, 4}}
	cycle, err := FindEulerCycle(nodes)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(cycle)

	// Define another graph
	// Define is it dicotyledonous
	// If it is then find a share
}
