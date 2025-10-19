from statistics import mean

def kpis_temp(tem_C, umbral=80.0):
    """KPIs de voltaje: n, min, max, prom, alertas y %."""
    tem_C = [float(v) for v in tem_C if v is not None]
    n = len(tem_C)
    if n == 0:
        return {"n":0,"min":None,"max":None,"prom":None,"alerts":0,"alerts_pct":0.0}
    alerts = sum(v > umbral for v in tem_C)
    return {
        "n": n,
        "min": min(tem_C),
        "max": max(tem_C),
        "prom": mean(tem_C),
        "alerts": alerts,
        "alerts_pct": 100.0 * alerts / n
    }