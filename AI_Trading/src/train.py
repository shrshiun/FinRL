from AI_Trading.src.stablebaselines3_models import DRLAgent as DRLAgent_sb3
from AI_Trading.src import config
from AI_Trading.src import model_config
from stable_baselines3.common.monitor import Monitor


def trainPortfolioAllocation(env_train, model_name, model_index):
    env_train = Monitor(env_train,filename=f'{config.LOG_PATH}a2c_{model_index}')
    env_train, _ = env_train.get_sb_env()
    agent = DRLAgent_sb3(env = env_train)

    if model_name == 'A2C':
        model_a2c = agent.get_model(model_name="a2c",model_kwargs = model_config.A2C_PARAMS)

        train_model = agent.train_model(model=model_a2c, 
                                tb_log_name='a2c',
                                total_timesteps=model_config.TOTAL_TIMESTEPS)
        train_model.save(config.TRAINED_MODEL_PATH + 'A2C_' +  str(model_index) + '.zip')

    elif model_name == 'PPO':
        model_ppo = agent.get_model("ppo",model_kwargs = model_config.PPO_PARAMS)
        train_model = agent.train_model(model=model_ppo, 
                             tb_log_name='ppo',
                             total_timesteps=80000)
        train_model.save(config.TRAINED_MODEL_PATH + 'PPO_'+  str(model_index) + '.zip')

    elif model_name == 'DDPG':
        model_ddpg = agent.get_model("ddpg",model_kwargs = model_config.DDPG_PARAMS)
        train_model = agent.train_model(model=model_ddpg, 
                             tb_log_name='ddpg',
                             total_timesteps= model_config.TOTAL_TIMESTEPS)
        train_model.save(config.TRAINED_MODEL_PATH + 'DDPG_'+  str(model_index) + '.zip')

    elif model_name == 'TD3':
        model_sac = agent.get_model("sac",model_kwargs = model_config.SAC_PARAMS)
        train_model = agent.train_model(model=model_sac, 
                             tb_log_name='sac',
                             total_timesteps= model_config.TOTAL_TIMESTEPS)
        train_model.save(config.TRAINED_MODEL_PATH + 'SAC_' +  str(model_index) + '.zip')

    elif model_name == 'SAC':
        model_td3 = agent.get_model("td3",model_kwargs = model_config.TD3_PARAMS)
        train_model = agent.train_model(model=model_td3, 
                             tb_log_name='td3',
                             total_timesteps=30000)
        train_model.save(config.TRAINED_MODEL_PATH + 'TD3_' +  str(model_index) + '.zip')