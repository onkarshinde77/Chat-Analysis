import matplotlib.pyplot as plt
import io
import base64

def make_chart_to_img(selected_user,X):
    if selected_user == "All Users":
        plt.title("Most Active Users")
        fig, ax = plt.subplots()
        ax.bar(X.index, X.values, color='red')
        plt.xticks(rotation='vertical')
        # plt.xticks(rotation=35)
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        return img_base64
