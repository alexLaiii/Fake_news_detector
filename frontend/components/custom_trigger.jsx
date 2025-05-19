
// This page is for the custom sidebar toggle, define the hover logic
import { useSidebar } from "@/components/ui/sidebar"
import { Tooltip, TooltipTrigger, TooltipContent } from "@/components/ui/tooltip";
import { Columns2Icon } from "lucide-react";


export function CustomTrigger() {
  const { toggleSidebar } = useSidebar();

  return (
    <Tooltip>
      <TooltipTrigger asChild>
        <button
          onClick={toggleSidebar}
          className="p-2 rounded hover:bg-gray-200 inline-flex items-center"
        >
          <Columns2Icon />
        </button>
      </TooltipTrigger>
      <TooltipContent side="right" align="center">
        Toggle Sidebar
      </TooltipContent>
    </Tooltip>
  );
}