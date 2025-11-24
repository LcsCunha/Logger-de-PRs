import matplotlib.pyplot as plt

def get_info(path):
    """Reads a file and return a date list and weight list"""
    lifts = {}

    with open(path, "r") as file:
        for line in file:
            if '-' and '->' in line:
                line = line.replace(" ", "")
                lift_name = line.split('-')[0]
                lift_date = line.split('->')[1].replace('\n', '')
                lift_weight = line.split('kg')[0].split('-')[1]
            
                if lift_name not in lifts.keys():
                    new_lift = {
                                lift_name:
                                    {
                                    "weights": [lift_weight],
                                    "dates": [lift_date],
                                    }  
                               }
                    lifts.update(new_lift)
                else:
                    lift = lifts.get(lift_name)
                    lift["weights"].append(lift_weight)
                    lift["dates"].append(lift_date)

                    lifts[lift_name] = lift

    return lifts

def build_graphs(lifts):
    """Receives the dates and the weights and plot as a graph"""

    for lift in lifts.keys():
        x = lifts[lift]["dates"]
        y = lifts[lift]["weights"]

        plt.plot(x, y)
        plt.xlabel("Cargas")
        plt.ylabel("Datas")
        plt.title(str(lift))
        plt.show()