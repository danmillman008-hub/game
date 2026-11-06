import type { MetadataRoute } from "next";

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "کنکور-میمو × لرن‌هارنس",
    short_name: "کنکور-میمو",
    description:
      "پلتفرم یادگیری تطبیقی کنکور با موتور میمو، گراف دانش KST، تسلط BKT و مرور فاصله‌دار FSRS-5.",
    start_url: "/",
    display: "standalone",
    orientation: "portrait",
    background_color: "#F6F7FB",
    theme_color: "#7E4BDE",
    dir: "rtl",
    lang: "fa",
    icons: [{ src: "/icon.svg", sizes: "any", type: "image/svg+xml", purpose: "any" }],
  };
}
