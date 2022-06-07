document.addEventListener("DOMContentLoaded",()=>{
    const leaveApplicationContent=document.querySelector("#create-leave-application");
    const leaveApprovalContent=document.querySelector("#leave-approval-status");
    const holidayCalendarContent=document.querySelector("#holiday-calendar-list");

    document.querySelector("#linkCreateLeaveApplication").addEventListener("click", (e)=>{
        e.preventDefault();
        leaveApplicationContent.style.display="block";
        leaveApprovalContent.style.display="none";
        holidayCalendarContent.style.display="none"

    });

    document.querySelector("#linkLeaveApprovalStatus").addEventListener("click",(e)=>{
        e.preventDefault();
        leaveApplicationContent.style.display="none";
        leaveApprovalContent.style.display="block";
        holidayCalendarContent.style.display="none"
        
       
    });

    document.querySelector("#linkHolidayCalendar").addEventListener("click",(e)=>{
        e.preventDefault();
        // leaveApplicationContent.classList.add("main-content-body");
        // leaveApprovalContent.classList.add("main-content-body");
        // holidayCalendarContent.classList.remove("main-content-body");
        leaveApplicationContent.style.display="none";
        leaveApprovalContent.style.display="none";
        holidayCalendarContent.style.display="block"
    });
});