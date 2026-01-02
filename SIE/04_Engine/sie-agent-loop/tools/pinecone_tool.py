# tools/pinecone_tool.py
from crewai.tools import tool
from pinecone import Pinecone
from openai import OpenAI
import os

# Initialize clients
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@tool("Knowledge Core Search")
def query_knowledge_core(query: str) -> str:
    """
    Search the SIE Knowledge Core (Pinecone) for existing intelligence.
    Use this FIRST before conducting external web searches to leverage 
    internal institutional knowledge and avoid redundant research.
    
    Args:
        query: The research question or topic to search for
        
    Returns:
        Relevant findings from the Knowledge Core, or indication if no prior intelligence exists
    """
    try:
        # Get index
        index_name = os.getenv("PINECONE_INDEX_NAME", "adambernard")
        index = pc.Index(index_name)
        
        # Generate embedding using text-embedding-3-small (512 dimensions)
        response = openai_client.embeddings.create(
            model="text-embedding-3-small",
            input=query
        )
        query_embedding = response.data[0].embedding
        
        # Search Pinecone
        results = index.query(
            vector=query_embedding,
            top_k=3,
            include_metadata=True
        )
        
        # Format results
        if not results.matches or len(results.matches) == 0:
            return f"Knowledge Core Search: No existing intelligence found on '{query}'. This is new territory - proceed with external research."
        
        # Extract relevant findings
        findings = []
        for match in results.matches:
            score = match.score
            metadata = match.metadata
            
            # Only include high-confidence matches (similarity > 0.7)
            if score > 0.7:
                content = metadata.get('text', 'No content available')
                source = metadata.get('source', 'Internal research')
                date = metadata.get('date', 'Unknown date')
                
                findings.append(f"**Match Score: {score:.2f}**\n{content}\nSource: {source} | Date: {date}")
        
        if not findings:
            return f"Knowledge Core Search: Found {len(results.matches)} low-confidence matches for '{query}'. Recommend fresh external research."
        
        return f"**Knowledge Core Intelligence Found:**\n\n" + "\n\n---\n\n".join(findings)
        
    except Exception as e:
        return f"Knowledge Core unavailable: {str(e)}. Proceeding with external search only."