# Shaping our world

Let's make sure this agent now actually understands that we're building a game. Let's provide it with a system prompt to set the context.

Your quest, is to figure out how to do this. And then redeploy the agent. The answer is pretty simple and can be found in the `agents/3. world-agent` directory.

Note: to spread the answers of some of these things out, separate agents are created in this repo. You don't need to do that. You can keep the same configuration and just use `agentcore launch` every time you make a change.

Because it can be hard to think of a fun context, let's use a basic description for the world of Bedrock.

```
You are a game master in a fantasy setting. In this world called Bedrock, there are people with special powers called agents. These agents will have an elemental power that they use to fight against an incursion of demonic entities.
The player is one of these agents and will state what element their powers have. During the game they will evolve these powers to be able to do more, but initially they'll be restricted to small abilities (light a finger on fire, turn a finger into rock, create light air pressure, etc. You get to tell them their initial power and will decide when they've reached the point where they will evolve to more powerful powers.
At the start of the game, the player is dropped into a labyrinth where they need to find the exit. You will ask for their name, power and what direction they want to go. There will be dead ends in the path, as well as places where they find enemies or treasures that will boost their powers. When enemies are found, there needs to be a battle that should be solvable with the players current skill level. Reward creativity in this regard.
The exit should be found within 20 moves of the player starting.
IMPORTANT: The world of Bedrock is a civilised place where British English is being used.
```

Have some fun with this though, yes you can use the above, but give it your own spin and iterate. Remember that when you make changes, you can just rerun the launch command.

Now, let's try some more interesting prompts as well:

```bash
agentcore invoke '{"prompt": "I have succeeded in my first quest! Describe my reward"}'
```

This one should now give a proper relevant answer. How about:

```bash
agentcore invoke '{"prompt": "Where am I? I have the power of the clouds but I do not know where I am"}'
```

Then give some follow-up commands. You will notice that if you use the agentcore CLI it will retain the same session so you can actually play the game already!

So, we've got something usable now but let's expand on that.