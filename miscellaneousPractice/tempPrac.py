# def largestPalindrome(n):
#     if n == 1:
#         return 9
#     high = 10 ** n
#     low = 10 ** (n - 1)
#     for i in range(high - 1, low - 1, -1):
#         w = int(str(i) + str(i)[::-1])
#         print(i, str(i)[::-1],w)
#         for i in range(high - 1, int(w ** 0.5) + 1, -1):
#             # print(w,i,int(w ** 0.5) + 1)
#             if w % i == 0:
#                 z = w // i
#                 if z < high and z >= low:
#                     return w % 1337
#
#
# print(largestPalindrome(2))



# /*
#     Time Complexity: O(N^2)
#     Space Complexity: O(N)
#
#     Where 'N' is the number of nodes in the given graph.
# */
#
# // Function for finding a cycle in the graph.
# bool findCycle(int src, vector<bool> &visited, vector<bool> &recStack, vector<int> adj[]) {
#     // Mark the node as visited.
#     visited[src] = true;
#
#     // Include the current node in the recursion Stack.
#     recStack[src] = true;
#
#     for (int i : adj[src]) {
#         // Back edge exists.
#         if (recStack[i] == true) {
#             return 1;
#         }
#
#         // Visit the unvisited adjacent nodes.
#         if (visited[i] == false) {
#             if (findCycle(i, visited, recStack, adj)) {
#                 return true;
#             }
#         }
#     }
#     // Remove the current node from the recursion stack.
#     recStack[src] = false;
#     return false;
# }
#
# // Function for doing a depth first search on the graph.
# int dfs(int src, vector<int> &freq, string &values, vector<int> adj[]) {
#
#     // Increment the frequency of the character assigned to the current node.
#     freq[values[src - 1] - 'a']++;
#
#     // To store the maximum frequency.
#     int maxValue = freq[values[src - 1] - 'a'];
#
#     // Iterate through the adjacent nodes.
#     for (int i : adj[src]) {
#         // Update the maximum value.
#         maxValue = max(maxValue, dfs(i, freq, values, adj));
#     }
#
#     // Decrement the frequency of the character assingned to the current node.
#     freq[values[src - 1] - 'a']--;
#
#     // Return the maximum frequency.
#     return maxValue;
# }
#
# int maxPathValue(int n, int m, vector<vector<int>> &edges, string &values) {
#
#     // Adjacency list.
#     vector<int> adj[n + 1];
#
#     // Iterate through the edges.
#     for (vector<int> i : edges) {
#         adj[i[0]].push_back(i[1]);
#     }
#
#     int ans = 0;
#
#     // For keeping track of visited nodes.
#     vector<bool> visited(n + 1, 0), recStack(n + 1, 0);
#
#     // For storing the frequency of the characters.
#     vector<int> freq(26, 0);
#
#     for (int i = 1; i <= n; i++) {
#         // Check if a cycle exists.
#         if (!visited[i] and findCycle(i, visited, recStack, adj)) {
#             return -1;
#         }
#     }
#
#     // Iterate through all the nodes.
#     for (int i = 1; i <= n; i++) {
#         fill(freq.begin(), freq.end(), 0);
#
#         // Do a DFS from the current node.
#         ans = max(ans, dfs(i, freq, values, adj));
#     }
#     return ans;
}