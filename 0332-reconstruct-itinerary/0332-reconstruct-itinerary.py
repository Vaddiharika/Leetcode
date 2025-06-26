class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic=collections.defaultdict(list)
        for src,dis in sorted(tickets,reverse=True):
            dic[src].append(dis)
            visited=[]
        def dfs(cur):
            while dic[cur]:
                dfs(dic[cur].pop())
            visited.append(cur)
        dfs("JFK")
        return visited[::-1]