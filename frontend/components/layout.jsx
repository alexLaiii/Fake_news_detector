import { SidebarProvider, SidebarTrigger, Sidebar } from "@/components/ui/sidebar";
import { AppSidebar } from "@/components/app-sidebar";
import { CustomTrigger } from "./custom_trigger";

export default function Layout({ children }) {
  return (
    
      <div className="flex min-h-screen">
        <SidebarProvider>
        <AppSidebar />
        <main className="flex-1 p-6">
          <CustomTrigger />
          {children}
        </main>
        </SidebarProvider>
      </div>
    
  );
}
