from pathlib import Path
import csv
from FUNCION.cleaning import clean_file
from FUNCION.kpis import kpis_temp
from FUNCION.plotting import plot_temperature_line, plot_temperature_hist, plot_boxplot_by_sensor
from FUNCION.IO_Utils import Root, ensure_dirs, list_raw_csvs, safe_stem, make_clean_name

# === Parámetros ===
ROOT = Root(__file__)
RAW_DIR = ROOT / "DATA" / "RAW"
PROC_DIR = ROOT / "DATA" / "PROCCESING"
PLOTS_DIR = ROOT / "plots"
REPORTS_DIR = ROOT / "Reportes"
UMBRAL_T = 80 # umbral de temperatura para alertas

ensure_dirs(RAW_DIR, PROC_DIR, PLOTS_DIR, REPORTS_DIR)

def main():
    raw_files = list_raw_csvs(RAW_DIR, pattern="*.csv")
    if not raw_files:
        print(f"No hay CSV en crudo en {RAW_DIR}"); return

    resumen_kpis = []
    sensor_to_tem = {}  # para el boxplot global

    for in_path in raw_files:
        # Nombre de salida limpio
        clean_name = make_clean_name(in_path)
        out_path = PROC_DIR / clean_name

        # 1) Limpiar y escribir CSV limpio
        ts, volts, Temperatura_C, stats = clean_file(in_path, out_path)
        if not ts:
            print("Sin datos válidos:", in_path.name)
            continue

        # 2) KPIs por archivo (voltaje)
        kv = kpis_temp(Temperatura_C, umbral=UMBRAL_T)
        resumen_kpis.append({
            "archivo": in_path.name,
            "salida": out_path.name,
            **stats,  # calidad
            "n": kv["n"], "min": kv["min"], "max": kv["max"],
            "prom": kv["prom"], "alerts": kv["alerts"], "alerts_pct": kv["alerts_pct"]
        })

        # 3) Gráficos por archivo
        stem_safe = safe_stem(out_path)
        plot_temperature_line(
            ts, Temperatura_C, UMBRAL_T,
            title=f"Temperatura vs Tiempo — {out_path.name}",
            out_path=PLOTS_DIR / f"{stem_safe}__temp_line__{UMBRAL_T:.1f}C.png"
        )
        plot_temperature_hist(
            Temperatura_C,
            title=f"Histograma Temperatura — {out_path.name}",
            out_path=PLOTS_DIR / f"{stem_safe}__temperatura_hist.png",
            bins=20
        )

        # 4) Acumular para boxplot global (sensor = id en nombre si aplica)
        # si tus archivos siguen formato 'voltaje_sensor_100XY.csv', etiqueta con 'S-100XY'
        name = out_path.stem
        sensor_id = name.replace("temperatura_sensor_", "")
        sensor_key = f"S-{sensor_id}" if sensor_id != name else name
        sensor_to_tem.setdefault(sensor_key, []).extend(volts)

    # 5) Guardar reporte KPIs
    rep_csv = REPORTS_DIR / "kpis_por_archivo.csv"
    with rep_csv.open("w", encoding="utf-8", newline="") as f:
        cols = ["archivo","salida","filas_totales","filas_validas","descartes_timestamp",
                "descartes_valor","%descartadas","n","min","max","prom","alerts","alerts_pct"]
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for row in resumen_kpis:
            w.writerow(row)
    print("Reporte KPIs:", rep_csv)

    # 6) Boxplot global por sensor
    if sensor_to_tem:
        plot_voltage_box = PLOTS_DIR / "boxplot_todos_sensores.png"
        plot_boxplot_by_sensor(sensor_to_tem, plot_voltage_box)
        print("Boxplot global:", plot_voltage_box)

if __name__ == "__main__":
    main()
    
    
