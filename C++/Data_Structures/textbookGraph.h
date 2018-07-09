class graphType
{
public:
    bool isEmpty() const;
    void createGraph();
    void clearGraph();
    void printGraph() const;
    void depthFirstTraversal();
    void dftAtVertex(int);
    void breadthFirstTraversal();
    graphType(int);
    ~graphType();

protected:
    int maxSize;
    int gSize;
    unorderedLinkedList<int> *graph;

private:
    void dft(int v, bool visited[]);
};

bool graphType::isEmpty() const
{
    return (gSize == 0);
}

void graphType::createGraph()
{
    int vertex;
    int adjacentVertex;
    if (gSize != 0) //if the graph is not empty, make it empty
        clearGraph();
    for (int index = 0; index < gSize; index++)
    {
        infile >> vertex;
        infile >> adjacentVertex;
        while (adjacentVertex != -999)
        {
            graph[vertex].insertLast(adjacentVertex);
            infile >> adjacentVertex;
        } //end while
    } // end for
} //end createGraph

void graphType::clearGraph()
{
    for (int index = 0; index < gSize; index++)
        graph[index].destroyList();
    gSize = 0;
} //end clearGraph

void graphType::printGraph() const
{
    for (int index = 0; index < gSize; index++)
    {
        cout << index << " ";
        graph[index].print();
        cout << endl;
    }
    cout << endl;
} //end printGraph

graphType::graphType(int size = 0)
{
    maxSize = size;
    gSize = 0;
    graph = new unorderedLinkedList<int>[size];
}
//Destructor
graphType::~graphType()
{
    clearGraph();
}