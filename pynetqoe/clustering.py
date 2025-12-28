from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

class UserClustering:
    def __init__(self, n_clusters=3):
        self.kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        self.scaler = StandardScaler()

    def profile_users(self, df):
        """Aggregates metrics by user_id and clusters them."""
        user_summary = df.groupby("user_id").agg({
            "QoA_VLCbitrate": "mean",
            "QoA_BUFFERINGcount": "mean",
            "MOS": "mean"
        }).dropna()
        
        scaled_data = self.scaler.fit_transform(user_summary)
        user_summary['cluster'] = self.kmeans.fit_predict(scaled_data)
        return user_summary