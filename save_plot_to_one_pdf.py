filename='Consolidation test.xlsx'
savefile=os.path.join(savePath,filename)
writer = pd.ExcelWriter(savefile)
for soil in soilType.values():
    df1 = df[df['soil Type']==soil]
    df1=df1.sort_values(by=['序号','stress'])
    df1.to_excel(writer, sheet_name=soil)
writer.save()

fig_width_cm = 21                         # A4 page 
fig_height_cm = 29.7 
inches_per_cm = 1 / 2.54              # Convert cm to inches 
fig_width = fig_width_cm * inches_per_cm # width in inches 
fig_height = fig_height_cm * inches_per_cm       # height in inches 
fig_size = [fig_width, fig_height] 


for soil in df['soil Type'].unique():
    df1 = df[df['soil Type']==soil]
    fig=plt.figure(2,figsize=fig_size,dpi=200)
    fig.clf()
    ax1 = fig.add_subplot(111)
    
    pdf_filename=os.path.join(savePath,'ConsolidationTest_plot_{}.pdf'.format(soil))
    pdf = PdfPages(pdf_filename )
    
    for k,sample in enumerate(df1['土样编号'].unique()):
        df2=df1[df1['土样编号']==sample]
        df2=df2.dropna(subset=['ei'])
        j=int((k-k%5)/5)
        if j==0:
            ax1.plot(df2['stress'],df2['deltaepsv'],'-o',label=sample)
        elif j==1:
            ax1.plot(df2['stress'],df2['deltaepsv'],'--*',label=sample)
        elif j==2:
            ax1.plot(df2['stress'],df2['deltaepsv'],'-.<',label=sample)
        else:
            ax1.plot(df2['stress'],df2['deltaepsv'],'-.>',label=sample)
            
            
    ax1.set_xscale("log")

    #ax1.set_xlabel('logStress')
    ax1.set_ylabel('deltaepsv')
    ax1.set_title('Soil type = {:>12s}\nStress(logScale)\n'.format(soil),fontweight='bold',color = 'blue', fontsize='12')
    
    #plt.xlabel('title of the xlabel', fontweight='bold', color = 'orange', fontsize='17', horizontalalignment='center') 

    ax1.set_xticks([50,100,200,400,600,800,1600])
    ax1.set_xticklabels([50,100,200,400,600,800,1600])
    ax1.invert_yaxis()
    ax1.xaxis.tick_top()
    ax1.grid()
    if k>6:            
        ax1.legend(loc='lower center', bbox_to_anchor=(1.05, 0.),   fancybox=True, shadow=True)
    else:
        ax1.legend()
    pdf.savefig() 
    pdf.close()    
 
Pdf_file_list = [] 
for soil in df['soil Type'].unique():       
    pdfFilename='ConsolidationTest_plot_{}.pdf'.format(soil)
    Pdf_file_list.append(pdfFilename)

merger = PdfFileMerger() 
for f in Pdf_file_list:     
    file=os.path.join(savePath,f) 	
    merger.append(PdfFileReader(file), 'rb') 
    os.remove(file)
  
merger.write(os.path.join(savePath,'ConsolidationTest_plot_all.pdf')) 
