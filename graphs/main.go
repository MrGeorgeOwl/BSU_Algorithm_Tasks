package main

// Node is struct for representing node of the graph
type Node struct {
	index      int
	neighbours []int
}

// Graph is struct for representing graph
type Graph struct {
	currentIndex int
	nodes        []Node
}

// NewGraph creates pointer to new Graph
func NewGraph(nodes ...[]int) *Graph {
	graph := Graph{1, make([]Node, 0)}

	for i := range nodes {
		graph.AddNode(nodes[i])
	}

	return &graph
}

// AddNode add Node constructed from nodes indexes to Graph
func (graph *Graph) AddNode(neighbours []int) {
	graph.nodes = append(graph.nodes, Node{graph.currentIndex, neighbours})
	graph.currentIndex++
}

func main() {

}
