import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // The Arena preview serves the dev server from *.e2b.app, so Next must accept
  // cross-origin requests for HMR and /_next assets.
  allowedDevOrigins: ["*.e2b.app", "*.alias.beta.e2b.app"],
  experimental: {
    optimizePackageImports: ["lucide-react"],
  },
};

export default nextConfig;
