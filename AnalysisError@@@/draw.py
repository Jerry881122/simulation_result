import matplotlib.pyplot as plt
import numpy as np



def draw():

    snr = [1, 1.5, 2, 2.5, 3, 3.5]

    miss_path_crc7 = np.array([4968, 4950, 4930, 4903, 4849, 4706])
    wrong_path_crc7 = np.array([33, 51, 71, 98, 152, 295])


    plt.plot(snr,miss_path_crc7/(miss_path_crc7+wrong_path_crc7),'-o',label="missing path")
    plt.plot(snr,wrong_path_crc7/(miss_path_crc7+wrong_path_crc7),'-o',label="wrong path")


    plt.xlabel("Eb/N0")
    plt.ylabel("rate")
    plt.legend()
    plt.grid(True)
    plt.minorticks_on()  # 啟用次要刻度
    plt.grid(which='minor', linestyle='-.', linewidth=0.8, alpha=0.3)  # 只針對次要刻度
    # if isOutputFile:
    #     plt.savefig(filename+"_draw_FER.jpg", dpi=300, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":

    draw()