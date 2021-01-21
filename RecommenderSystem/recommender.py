from lightfm import LightFM
import numpy as np
from fetch_data import fetch_data

def recommendation(model, data, users):
    num_items = data.shape[1]

    for user in users:
        scores = model.predict(user, np.arange(num_items))
        top_items = np.argsort(-scores)

        print(f'Recommendations for User {user}')

        for x in top_items[:3]:
            print(f'\t{x}')

def main():
    data = fetch_data()

    warp = LightFM(loss='warp')
    logistic = LightFM(loss='logistic')
    bpr = LightFM(loss='bpr')

    warp.fit(data['matrix'],epochs=30,num_threads=2)
    logistic.fit(data['matrix'],epochs=30, num_threads=2)
    bpr.fit(data['matrix'],epochs=30, num_threads=2)

    print('Using the WARP loss function: ')
    recommendation(model=warp,data=data['matrix'], users=[20, 23, 50])
    print('\n')

    print("Using the Logistic loss function")
    recommendation(model=logistic, data=data['matrix'], users=[20,23, 50])
    print('\n')

    print("Using the BPR loss function")
    recommendation(model=bpr, data=data['matrix'], users=[20,23, 50])
    print('\n')

if __name__ == "__main__":
    main()