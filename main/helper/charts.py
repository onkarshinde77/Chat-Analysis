import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import io
import base64

def active_user_to_img(selected_user,X):
    if selected_user == "All Users":
        plt.title("Most Active Users")
        fig, ax = plt.subplots()
        ax.bar(X.index, X.values, color='red')
        plt.xticks(rotation='vertical')
        plt.tight_layout()
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close(fig)
        return img_base64
    else: return None
    
def timeline_chart(timeline):
    fig ,ax = plt.subplots()
    if timeline.shape[0] > 1:
        ax.plot(timeline['month_year'], timeline['messages'], color='red')
    elif timeline.shape[0] == 1:
        ax.scatter(timeline['month_year'], timeline['messages'], color='red')
    else:
        plt.close(fig)
        raise ValueError("DataFrame is empty. Nothing to plot.")
    plt.xticks(rotation="vertical")
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return img_base64
    
    
