package main

import "fmt"

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

	// Define another graph
	// Find Euler cycle

	// Define another graph
	// Define is it dicotyledonous
	// If it is then find a share
}
