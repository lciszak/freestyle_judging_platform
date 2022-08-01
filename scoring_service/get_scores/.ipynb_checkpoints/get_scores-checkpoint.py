#---------------------
#-- main function
#---------------------
import pandas as pd

def get_scores(sheet_id = "1xl5j4HdofudpJ1A1BmJC5JmES81k25um_AmP79xQDVY"):
    try:
        #-- scores
        sheet_name = "scores_raw"
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
        df_scores=pd.read_csv(url)

        #-- drop empty results
        empty=len(df_scores.Judge.value_counts()) <= 0

        if empty:
            html_result="<html><head></head><body>No results to summarize</body></html>"
            return html_result
        
        #-- riders
        sheet_name = "Riders"
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
        df_riders=pd.read_csv(url)
        
        #-- keep only relevant columns
        df_rider_small=df_riders[['Rider','Division']]
        df_score_small=df_scores[['Judge','Rider','Round','Run','total_score']].copy()
        df_score_detail=df_score_small.merge(df_rider_small,on=["Rider"])

        #-- fill NA with zeros

        df_score_detail=df_score_detail.fillna(0)
        #-- aggregate results
        run_agg=df_score_detail[['Rider','Round','Run','total_score','Division']].groupby(['Division','Round','Rider','Run'],as_index=False).aggregate(['min','max','sum','count']).droplevel(axis=1, level=[0]).reset_index()

        #-- standardize the score
        def stand_score(row):
            if row['count']>=3:
                res=(row['sum']-row['min']-row['max'])/(row['count']-2)
            else:
                res=row['sum']/row['count']
            return res

        run_agg['normalized_score']=run_agg.apply(stand_score,axis=1)

        #-- get the best run
        run_agg_best=run_agg[['Division','Round','Rider','normalized_score']].groupby(['Division','Round','Rider']).aggregate(max).reset_index()
        run_agg_best.columns=["Division","Round","Rider","Normalized Score"]

        #-- one table per division and round
        divisions=list(set(run_agg_best.Division))

        #-- prepare results in HTML
        html_result="<html><body>\n"
        html_result+="<h1>EFSC 2022 results</h1>\n"
        #-- qualifiers
        html_result+="<h2>Qualifiers</h2>\n"
        for division in divisions:
            html_result+="<h3>"+division+"</h3>\n"
            current_grp=run_agg_best[(run_agg_best.Division==division) & (run_agg_best.Round=="Qualifiers")].sort_values(by="Normalized Score",ascending=False).copy()
            tmp=current_grp.to_html(index=False)
            html_result+=tmp+"\n"

        #-- finals
        html_result+="<br>\n"
        html_result+="<h2>Finals</h2>\n"
        for division in divisions:
            html_result+="<h3>"+division+"</h3>\n"
            current_grp=run_agg_best[(run_agg_best.Division==division) & (run_agg_best.Round=="Finals")].sort_values(by="Normalized Score",ascending=False).copy()
            tmp=current_grp.to_html(index=False)
            html_result+=tmp+"\n"

        html_result+="</body></html>"
    except Exception as e:
        html_result="<html><head></head><body>"+str(e)+"</body></html>"
    
    return(html_result)