import yfinance as yf
import mplfinance as mpf
import matplotlib.pyplot as plt

# Hisse senedi verilerini indirme ve grafik analizi
def hisse_grafik_analiz(hisse_kodu, baslangic_tarihi, bitis_tarihi):
    # Hisse senedi verilerini yfinance kullanarak indirme
    veri = yf.download(hisse_kodu, start=baslangic_tarihi, end=bitis_tarihi)

    # MPLFinance ile mum grafikleri çizimi
    mpf.plot(veri, type='candle', volume=True, show_nontrading=True, style='charles',
             title=f'{hisse_kodu} Hisse Senedi', ylabel='Fiyat ($)', ylabel_lower='Volume (Milyon)')

    # Basit bir grafik formasyonu ekleyelim (örnek amaçlı)
    fig, ax = plt.subplots()
    ax.plot(veri.index, veri['Close'], label='Kapanış Fiyatı', color='blue')
    ax.plot(veri.index, veri['High'], label='En Yüksek Fiyat', color='green')
    ax.plot(veri.index, veri['Low'], label='En Düşük Fiyat', color='red')
    ax.set_title(f'{hisse_kodu} Hisse Senedi Fiyat Grafiği')
    ax.set_xlabel('Tarih')
    ax.set_ylabel('Fiyat ($)')
    ax.legend()
    ax.grid(True)
    
    # Grafik formasyonunu işaretleyelim (örnek amaçlı, gerçek bir formasyon değildir)
    ax.annotate('Örnek Formasyon', xy=(veri.index[-10], veri['Close'][-10]),
                xytext=(veri.index[-20], veri['Close'][-20]),
                arrowprops=dict(facecolor='black', arrowstyle='->'),
                fontsize=12)

    plt.show()

# Örnek olarak Apple hisse senedi (AAPL) için analiz yapalım
hisse_kodu = 'BIMAS.IS'
baslangic_tarihi = '2023-01-01'
bitis_tarihi = '2024-01-01'

hisse_grafik_analiz(hisse_kodu, baslangic_tarihi, bitis_tarihi)
