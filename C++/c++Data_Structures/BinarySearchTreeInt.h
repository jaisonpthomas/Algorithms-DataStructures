// Implementation based on Tony Gaddis' "C++: From Control Structures through Objects
// with modifications

#ifndef INT_BINARY_SEARCH_TREE_H
#define INT_BINARY_SEARCH_TREE_H

class IntBinarySearchTree
{
private:
    struct TreeNode
    {
        int value;
        TreeNode* left;
        TreeNode* right;
    };
    TreeNode* root;

    void insertNode(TreeNode*&, TreeNode*&);        //TreeNode*& creates a direct-reference to a TreeNode*
    //DeleteFunctions
    void destroySubTree(TreeNode*);
    void deleteNode(int, TreeNode*&);
    void makeDeletion(TreeNode*&);
    
    int getHeight(TreeNode*);

    //DisplayFunctions
    void displayInOrder(TreeNode*) const;
    void displayPreOrder(TreeNode*) const;
    void displayPostOrder(TreeNode*) const;
    void displayLevelOrder(TreeNode*) const;    //FUTURE: NEED TO IMPLEMENT


public:
    //Constructor
    IntBinarySearchTree()
    { root = nullptr; }                         //FUTURE: NEED TO IMPLEMENT COPY CONSTRUCTOR
    //Destructor
    ~IntBinarySearchTree()
    { destroySubTree(root); }

    void insert(int);
    void remove(int);
    void search(int);

    int getHeight()
    { getHeight(root); }

    void displayInOrder() const
    { displayInOrder(root); }
    void displayPreOrder() const
    { displayPreOrder(root); }
    void displayPostOrder() const
    { displayPostOrder(root); }
};

void IntBinarySearchTree::insert(int num)
{
    TreeNode* newNode = new TreeNode;
    newNode->value = num;
    newNode->left = newNode->right = nullptr;

    insert(root, newNode);
}

void IntBinarySearchTree::insertNode(TreeNode*& root, TreeNode*& newNode)
{
    if(!root)
        root = newNode;
    else if (newNode->value < root->value)
        insert(root->left, newNode);
    else
        insert(root->right, newNode);
}

void IntBinarySearchTree::remove(int num)
{
    deleteNode(num, root);
}

void IntBinarySearchTree::deleteNode(int num, TreeNode*& localRoot)
{
    if(num < localRoot->value)
        deleteNode(num, localRoot->left);
    else if(num > localRoot->value)
        deleteNode(num, localRoot->right);
    else if(num == localRoot->value)
        makeDeletion(localRoot);
    else
        cout << "Cannot delete value from tree: not currently present in list"
}

void IntBinarySearchTree::makeDeletion(TreeNode*& delNode)
{
    TreeNode* temp = nullptr;

    if(!delNode)
        cout << "Cannot delete empty node" << endl;
    
    //Deleting Node with 0-1 Children (left child)
    else if(!(delNode->right))
    {
        temp = delNode;
        delNode = delNode->left;
        delete temp;
    }
    //Deleting Node with 1 right Child
    else if(!(delNode->left))
    {
        temp = delNode;
        delNode = delNode->right;
        delete temp;
    }
    //Deleting Node with 2 Children
    else
    {
        //ALGORITHM:
            //1. Find sucessor node (smallest on right branch)
            //2. sucessor.left gets pointed to delNode's left item
            //    2.1 temp pointer becomes delNode (temp now just a pointer for deletion)
            //3. delNode pointer moved onto delNode.right (removing delNode from tree)
            //    3.1 temp deleted

        //Step 1
        temp = delNode->right;
        while(temp->left)
            temp = temp->left;
        //Step 2
        temp->left = delNode->left;
        //Step 2.1
        temp = delNode;
        //Step 3
        delNode = delNode->right;
        //Step 3.1
        delete temp;
    }
}

bool IntBinarySearchTree::search(int searchVal)
{
    TreeNode* localRoot = root;

    while(localRoot)
    {
        if(searchVal == localRoot->value)
            return true;
        else if(searchVal > localRoot->value)
            localRoot = localRoot->right;
        else
            localRoot = localRoot->left;
    }
    return false;
}

int IntBinarySearchTree::getHeight (TreeNode* nodePtr)
{
    if(!nodePtr)
        return 0;
    else
        return 1 + max(getHeight(nodePtr->left), getHeight(nodePtr->right);
}

void IntBinarySearchTree::displayInOrder(TreeNode* root) const
{
    if(root)
    {
        displayInOrder(root->left);
        cout << root->value << endl;
        displayInOrder(root->right);
    }
}

void IntBinarySearchTree::displayPreOrder(TreeNode* root) const
{
    if(root)
    {
        cout << root->value << endl;
        displayPreOrder(root->left);
        displayPreOrder(root->right);
    }
}

void IntBinarySearchTree::displayPostOrder(TreeNode* root) const
{
    if(root)
    {
        displayInOrder(root->left);
        displayInOrder(root->right);
        cout << root->value << endl;
    }
}

#endif