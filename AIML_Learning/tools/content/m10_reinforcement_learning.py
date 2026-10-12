from common import *
NUM, FILE = "10", "10_Reinforcement_Learning"
TITLE = "Reinforcement Learning"
DESC = "Agents that learn by interacting with environments - from bandits to deep RL and RLHF."
TOPICS = [
 T("RL basics: agent, environment, state, action, reward, policy", B, "An agent observes a state, takes an action, gets a reward and next state; goal is to maximise cumulative discounted return.", "Agent action edukkum, environment reward tharum. Total reward maximize.",
   "import gymnasium as gym\ne=gym.make('CartPole-v1');s,_=e.reset(seed=0);tot=0\nfor _ in range(200):\n    s,r,t,tr,_=e.step(e.action_space.sample());tot+=r\n    if t or tr: break\nprint(tot)"),
 T("Multi-armed bandits, exploration vs exploitation", B, "Epsilon-greedy, UCB, Thompson sampling balance trying new options and using the best known.", "Explore vs exploit. epsilon-greedy.",
   "import numpy as np\nq=np.zeros(3);n=np.zeros(3);p=[.2,.5,.8]\nfor _ in range(2000):\n    a=np.random.randint(3) if np.random.rand()<.1 else q.argmax()\n    r=float(np.random.rand()<p[a]);n[a]+=1;q[a]+=(r-q[a])/n[a]\nprint(q.round(2))"),
 T("Markov Decision Processes, Bellman equations", I, "MDP = (S, A, P, R, gamma). V(s)=max_a [R + gamma * sum P V(s')] - the Bellman optimality equation.", "MDP, Bellman equation - RL-oda maths base.",
   yt_q="markov decision process bellman equation explained"),
 T("Dynamic programming: policy and value iteration", I, "Solve known MDPs by iterating policy evaluation/improvement or value updates.", "Policy iteration, value iteration.",
   "import numpy as np\nV=np.zeros(2);P=np.array([[.9,.1],[.2,.8]]);R=np.array([1,0])\nfor _ in range(200): V=R+.9*P@V\nprint(V)"),
 T("Monte Carlo and Temporal-Difference learning, SARSA, Q-learning", I, "Learn from experience without a model. Q-learning: Q(s,a) += alpha*(r + gamma*max Q(s',a') - Q(s,a)).", "Q-learning table-la values update pannum.",
   "import gymnasium as gym,numpy as np\ne=gym.make('FrozenLake-v1',is_slippery=False);Q=np.zeros((16,4))\nfor ep in range(2000):\n    s,_=e.reset()\n    for _ in range(100):\n        a=np.random.randint(4) if np.random.rand()<.2 else Q[s].argmax()\n        s2,r,t,tr,_=e.step(a);Q[s,a]+=.1*(r+.95*Q[s2].max()-Q[s,a]);s=s2\n        if t or tr: break\nprint(Q.argmax(1))"),
 T("Deep Q-Networks (DQN) and variants", A, "Neural network approximates Q; replay buffer + target network stabilise; Double/Dueling/Prioritised/Rainbow variants.", "DQN: Q-table-ku bathil neural network.",
   "from stable_baselines3 import DQN\n# DQN('MlpPolicy','CartPole-v1').learn(20000)"),
 T("Policy gradients: REINFORCE, Actor-Critic, A2C/A3C", A, "Directly optimise the policy with gradient ascent on expected return; critics reduce variance.", "Policy directly optimize - REINFORCE, actor-critic.",
   yt_q="policy gradient reinforce actor critic explained"),
 T("PPO, TRPO, SAC, DDPG, TD3", A, "Modern algorithms. PPO is the practical default; SAC/TD3 for continuous control.", "PPO most popular. SAC/TD3 continuous actions.",
   "from stable_baselines3 import PPO\nm=PPO('MlpPolicy','CartPole-v1',verbose=0).learn(10000)"),
 T("Model-based RL, planning, MCTS, AlphaGo/AlphaZero/MuZero", A, "Learn or use a model of the environment to plan; MCTS + neural networks mastered Go and chess.", "AlphaGo - MCTS + neural net.",
   yt_q="alphazero explained mcts"),
 T("Multi-agent RL, imitation learning, offline RL, inverse RL", A, "Cooperation/competition among agents, learning from demonstrations, learning from fixed datasets.", "Multi-agent, imitation, offline RL.",
   yt_q="multi agent reinforcement learning introduction"),
 T("RLHF and RL for LLM reasoning (PPO, GRPO, DPO)", A, "Use human or verifiable rewards to align and improve reasoning in language models.", "RLHF, GRPO - LLM-a improve panna RL.",
   yt_q="grpo rlhf reasoning models explained"),
 T("RL projects: CartPole, FrozenLake, Atari, trading bot, robot sim", I, "Start with Gymnasium classic control, then Atari/MuJoCo; always plot learning curves over multiple seeds.", "CartPole -> Atari -> custom env.",
   yt_q="reinforcement learning project gymnasium stable baselines3"),
]
