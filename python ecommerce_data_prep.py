```python
import pandas as pd

def clean_ecommerce_sales():
    print("Memproses laporan jualan e-dagang (TikTok Shop / Shopee)...")
    
    # Data mentah simulasi dengan ralat biasa (nilai kosong dan berulang)
    data = {
        'Order_ID': ['TK101', 'TK102', 'SH201', 'TK101', None],
        'Product': ['Baju Melayu', 'Kurta', 'T-Shirt', 'Baju Melayu', 'Kasut'],
        'Status': ['Completed', 'Pending', 'Cancelled', 'Completed', 'Completed'],
        'Platform': ['TikTok', 'TikTok', 'Shopee', 'TikTok', 'Shopee']
    }
    
    df = pd.DataFrame(data)
    print("\nData Asal:")
    print(df)
    
    print("\nMembersihkan data...")
    # Membuang baris yang tiada Order_ID (null)
    df_cleaned = df.dropna(subset=['Order_ID'])
    
    # Membuang data jualan yang direkod dua kali (duplicates)
    df_cleaned = df_cleaned.drop_duplicates()
    
    # Menapis hanya pesanan yang telah selesai untuk dimasukkan ke dashboard
    df_cleaned = df_cleaned[df_cleaned['Status'] == 'Completed']
    
    print("\nData yang telah dibersihkan (Sedia untuk Power BI/Tableau):")
    print(df_cleaned)
    
    # Menyimpan fail ke format CSV yang bersih
    print("\nMenyimpan fail ke 'clean_ecommerce_sales.csv'...")
    df_cleaned.to_csv('clean_ecommerce_sales.csv', index=False)
    print("Proses Selesai!")

if __name__ == "__main__":
    clean_ecommerce_sales()

