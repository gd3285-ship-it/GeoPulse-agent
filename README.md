<div align="center">
  <h1>🎯 GEOPulse: Generative Engine Optimization Agent</h1>
  <p><b>מפסיקים לנחש – מתחילים להשפיע על החלטות ה-AI</b></p>
</div>

<br/>

<div align="center">
  <h3>🎥 המערכת בפעולה</h3>
  
  https://github.com/user-attachments/assets/2ae92049-3398-4663-9a5b-ec753b074fd4

</div>

<br/>

<div align="center">
  <h3>📸 צילומי מסך מהמערכת</h3>
  <p align="center">
    <img src="https://github.com/user-attachments/assets/762a954d-746f-4665-9fac-b342a12f3ec6" width="48%" style="border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);" />
    <img src="https://github.com/user-attachments/assets/46a4d801-e42b-4733-a96f-58467ffaefbd" width="48%" style="border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);" />
  </p>
</div>

---

## 📌 אודות הפרויקט
פרויקט גמר מצטיין במסגרת האקתון עבור **"ביטוח ישיר"**. 

**GEOPulse** היא מערכת מודיעין ואופטימיזציה (GEO) מהפכנית שנועדה לפצח את "הקופסה השחורה" של מנועי ה-AI. המערכת מספקת מענה לצורך עסקי קריטי: חקירה ופענוח של מנגנוני ההמלצה וקבלת ההחלטות הפנימיים של מודלי שפה גדולים (LLMs). היא מאפשרת למנהלי שיווק להבין מדוע ה-AI מעדיף מתחרים, ולשלוט בנרטיב המותג בצורה אקטיבית מבוססת נתונים.

## 🚀 פיצ'רים מרכזיים (The Game Changers)
* º **פיצוח מנועי ה-AI והנדסה לאחור (Reverse Engineering):** חקירה ופענוח של מנגנוני ההמלצה וקבלת ההחלטות הפנימיים של מנועי ה-AI. המערכת מחליפה שבועות של מחקר ידני על ידי סריקה אוטומטית של מאות שאילתות.
* º **סוכן קופירייטינג אוטונומי (The Content Agent):** יצירת טיוטות תוכן שיווקי מתקן המבוסס על אופטימיזציה של נתוני אמת, במטרה להשפיע על דירוג המותג בהמלצות עתידיות (Reverse-SEO).
* º **Streaming UI מבוסס SSE:** חווית משתמש חיה וללא השהיות. הזרמה של "תהליכי החשיבה" של הסוכן והתקדמות הסריקה ישירות לדשבורד בזמן אמת.
* º **100% Hallucination-Free:** שימוש בארכיטקטורת RAG ומסד נתונים וקטורי לשליפת נתוני אמת מאומתים מאתר החברה בלבד.

---

## 🧠 ארכיטקטורת המערכת (Workflow)

```text
[ מנהל שיווק ]
     │
     ▼ (בקשת API)
[ שרת ה-Backend ] 
     │
     ├──▶ 🤖 מנועי AI (סריקה ואיסוף נתונים מ-GPT, Gemini, Perplexity)
     ├──▶ 📊 ניתוח סנטימנט (עיבוד 12 קטגוריות אסטרטגיות)
     ├──▶ 📚 ארכיטקטורת RAG (שליפת נתוני אמת מ-Pinecone)
     └──▶ ✍️ סוכן קופירייטינג (ג'ינרוט תוכן שיווקי מתקן)
     │
     ▼ (הזרמת נתונים חיה - SSE Streaming)
[ מרכז בקרה - React Dashboard ]
🛠️ סטק טכנולוגיצד לקוח (Frontend)צד שרת (Backend)AI & Data InfrastructureReactPythonGPT-4o, Gemini, PerplexityTypeScriptFastAPILlamaIndex WorkflowsEventSource (SSE)PostgreSQLPinecone (Vector DB)Lucide-ReactSQLAlchemyRAG Architecture
