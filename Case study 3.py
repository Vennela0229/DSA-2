import java.util.*;

static Set<String> bfsBounded(

Map<String,List<String>> adj,

String source,

int maxDepth){

Set<String> visited=
new HashSet<>();

visited.add(source);

Deque<Object[]> queue=
new ArrayDeque<>();

queue.offer(
new Object[]{
source,0});

Set<String> reached=
new HashSet<>();

while(!queue.isEmpty()){

Object[] cur=
queue.poll();

String u=
(String)cur[0];

int depth=
(int)cur[1];

if(!u.equals(source))
reached.add(u);

if(depth==maxDepth)
continue;

for(String v:
adj.getOrDefault(
u,
Collections.emptyList())){

if(!visited.contains(v)){

visited.add(v);

queue.offer(
new Object[]{
v,
depth+1});
}
}
}

return reached;
}
