struct Node
{
    int data;
    Node* left;
    Node* right;
}

bool checkBST(Node* root)
{ return checkBSTHelper(root, -1000000, 1000000); }


bool checkBSTHelper(Node* root, int min, int max)
{
    if(!root)
        return true;
    if (root->data <= min || root->data >= max)
        return false;
    return checkBSTHelper(root->left, min, root->data) &&
           checkBSTHelper(root->right, root->data, max);
}