import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path

def plot_temperature_line(ts, tem_C, umbral_v: float, title: str, out_path: Path):
    plt.figure(figsize=(9,4))
    plt.plot(ts, tem_C, label="Temperatura_C (%)")
    alerts_t = [t for t, v in zip(ts, tem_C) if v > umbral_v]
    alerts_v = [v for v in tem_C if v > umbral_v]
    plt.scatter(alerts_t, alerts_v, label=f"Alertas (> {umbral_v} %)")
    plt.axhline(umbral_v, linestyle="--", label=f"Umbral {umbral_v} %")
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
    plt.title(title); plt.xlabel("Tiempo"); plt.ylabel("Temperatura_C")
    plt.grid(True); plt.legend(); plt.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=150); plt.show()

def plot_temperature_hist(tem_C, title: str, out_path: Path, bins: int = 20):
    plt.figure(figsize=(6,4))
    plt.hist(tem_C, bins=bins)
    plt.title(title); plt.xlabel("Temperatura_C"); plt.ylabel("Frecuencia")
    plt.grid(True); plt.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=150); plt.show()

def plot_boxplot_by_sensor(sensor_to_tem: dict[str, list[float]], out_path: Path):
    labels = list(sensor_to_tem.keys())
    data = [sensor_to_tem[k] for k in labels if sensor_to_tem[k]]
    if not data:
        raise RuntimeError("No hay datos para boxplot.")
    horizontal = len(labels) > 10
    plt.figure(figsize=(max(8, len(labels)*0.8) if not horizontal else 8,
                        5 if not horizontal else max(6, len(labels)*0.6)))
    plt.boxplot(data, vert=not horizontal, showmeans=True)
    if horizontal:
        plt.yticks(range(1, len(labels)+1), labels)
        plt.xlabel("Temperatura C"); plt.ylabel("Sensor")
    else:
        plt.xticks(range(1, len(labels)+1), labels, rotation=60)
        plt.ylabel("Temperatura C"); plt.xlabel("Sensor")
    plt.title("Boxplot de temperatura por Sensor")
    plt.grid(True, axis="y" if not horizontal else "x")
    plt.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=150); plt.show()