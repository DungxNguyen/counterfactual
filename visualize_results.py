import matplotlib.pyplot as plt
import os

def plot_predictions(target, predictions, rmse, rmse_test, state_idx, args):
    fig = plt.figure()
    plt.plot(target[-4*7:])
    plt.plot(predictions[-4*7:])
    plt.title('Training RMSE: {:.2f} Testing RMSE: {:.2f}'.format(rmse, rmse_test))
    plt.xlabel("TimeStamp")
    plt.ylabel("Mortality Number")
    plt.legend(["Ground-truth", "Predictions"])
    Delta = args.Delta
    x = args.x
    if Delta == 0:
        fig.savefig(os.path.join("Figure-Prediction", f"State_{state_idx}_{args.date}.png"))
    else:
        fig.savefig(os.path.join("Figure-Prediction", f"State_{state_idx}_{args.date}_Delta_{Delta}_x_{x}.png"))


def plot_losses(losses, params, args):
    disease = params['disease']
    if params['joint']:
        FIGPATH = f'./Figures/{disease}/joint/'
    else:
        county_id = params['county_id']
        FIGPATH = f'./Figures/{disease}/{county_id}/'
    if not os.path.exists(FIGPATH):
        os.makedirs(FIGPATH)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(losses)
    date = params['date']
    fig.savefig(FIGPATH+f'/losses_{date}_{args.privacy}.png')
