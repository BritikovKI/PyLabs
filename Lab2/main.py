import base_client
import friend_list
import user
import matplotlib.pyplot as plt


def main():
    id = user.user()
    f_list = friend_list.friend_list()
    id.get_params()
    f_list.get_resp(id.vk_id)
    f_list.get_headers()
    plt.hist(f_list.stats, 40)
    plt.show()


main()
