# Idea Corner
## Tools
 - [SUMO-RL Repo](https://github.com/LucasAlegre/sumo-rl)
 - [CityFlow Repo](https://github.com/cityflow-project/CityFlow)
 - [Challenges of MARL](https://arxiv.org/pdf/2003.05738.pdf)
 - [Tutorials - Reinforcement Learning for Traffic Signal Control ](https://traffic-signal-control.github.io/)
 - [Inductive Graph Reinforcement Learning for Massive-Scale Traffic Signal Control](https://github.com/FXDevailly/IG-RL)

## things to decide 
1. Grid vs Real world?
2. Uniform grid or heterogeneous network e.g. 3/4 street intersections ?
3. Reward 
	- mean 
	- speed 
	- co2
	- throuput
4. Action
	- 0/ 1 green time split 
	- 0/1/2 skip next
	- phase selection (+ time)
	- once per cycle (60 sec) predict next cycle, (order + duration)
	(need predefined phases)
5.  State
	- coordinates
	- graph encoding 
		- smallest distance
		- like positional encoding
	- street
		- mean speed
		- number of cars
	- traffic light 
		- how long green
		- which side has green
		- number of connections
6. Model
	- same intersection, weight sharing, same model?
	- how to map streets to input dimension?
	- GNN or not?
	- transformer 
		- autoregressive?
		- Bert 
			- classify 0,1
7. Benchmark
	- sumo-rl
	- ring with 1 car and see if it can drive continuous
