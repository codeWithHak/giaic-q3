import streamlit as st
import json
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Custom CSS (unchanged)
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 1rem;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: 600;
        color: #2563EB;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    .book-card {
        background-color: #F3F4F6;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
        border-left: 5px solid #3B82F6;
    }
    .book-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #1F2937;
    }
    .book-author {
        font-size: 1rem;
        color: #4B5563;
    }
    .book-details {
        font-size: 0.9rem;
        color: #6B7280;
    }
    .read-badge {
        background-color: #10B981;
        color: white;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.8rem;
    }
    .unread-badge {
        background-color: #F59E0B;
        color: white;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.8rem;
    }
    .stat-card {
        background-color: #EFF6FF;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stat-number {
        font-size: 2rem;
        font-weight: 700;
        color: #2563EB;
    }
    .stat-label {
        font-size: 1rem;
        color: #4B5563;
    }
</style>
""", unsafe_allow_html=True)

# Load and save functions (unchanged)
def load_library():
    try:
        if os.path.exists("library.json"):
            with open("library.json", "r") as file:
                return json.load(file)
        else:
            return []
    except Exception as e:
        st.error(f"Error loading library file: {e}. Starting with an empty library.")
        return []

def save_library(library):
    try:
        with open("library.json", "w") as file:
            json.dump(library, file, indent=4)
        return True
    except Exception as e:
        st.error(f"Error saving library: {e}")
        return False

# Display book card (unchanged)
def display_book_card(book, i, is_search=False):
    col1, col2 = st.columns([5, 1])
    
    with col1:
        st.markdown(f"""
        <div class="book-card">
            <div class="book-title">{book.get('title', 'Unknown Title')}</div>
            <div class="book-author">by {book.get('author', 'Unknown Author')}</div>
            <div class="book-details">
                Published: {book.get('publication_year', 'Unknown')} | 
                Genre: {book.get('genre', 'Unknown')} | 
                <span class="{'read-badge' if book.get('read_status', False) else 'unread-badge'}">
                    {"Read" if book.get('read_status', False) else "Unread"}
                </span>
            </div>
            {f"<div class='book-details'>Notes: {book.get('notes', '')}</div>" if book.get('notes') else ""}
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if st.button("Edit", key=f"{'search_' if is_search else ''}edit_{i}"):
            st.session_state.edit_book = book
            st.session_state.show_add_form = True
            st.session_state.current_page = "Add Book"
            st.rerun()
        
        if st.button("Delete", key=f"{'search_' if is_search else ''}delete_{i}"):
            st.session_state.library.remove(book)
            save_library(st.session_state.library)
            st.success(f"'{book.get('title')}' has been removed from your library.")
            st.rerun()
        
        if not book.get('read_status', False):
            if st.button("Mark Read", key=f"{'search_' if is_search else ''}read_{i}"):
                book['read_status'] = True
                book['date_read'] = datetime.now().strftime("%Y-%m-%d")
                save_library(st.session_state.library)
                st.success(f"'{book.get('title')}' marked as read.")
                st.rerun()

# Initialize session state (unchanged)
if 'library' not in st.session_state:
    st.session_state.library = load_library()
if 'filtered_library' not in st.session_state:
    st.session_state.filtered_library = st.session_state.library
if 'show_add_form' not in st.session_state:
    st.session_state.show_add_form = False
if 'edit_book' not in st.session_state:
    st.session_state.edit_book = None
if 'reading_challenge' not in st.session_state:
    st.session_state.reading_challenge = 0
if 'filter_option' not in st.session_state:
    st.session_state.filter_option = "All Books"
if 'sort_option' not in st.session_state:
    st.session_state.sort_option = "Title (A-Z)"
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Library"

# App header (unchanged)
st.markdown('<h1 class="main-header">📚 Personal Library Manager</h1>', unsafe_allow_html=True)

# Sidebar with fixed navigation (unchanged)
with st.sidebar:
    st.markdown('<h2 class="section-header">Navigation</h2>', unsafe_allow_html=True)
    
    menu_options = ["Library", "Add Book", "Search Books", "Statistics", "Reading Challenge", "Import/Export"]
    
    def update_page():
        st.session_state.current_page = st.session_state.nav_selection
    
    st.radio(
        "Choose an option:",
        menu_options,
        index=menu_options.index(st.session_state.current_page),
        key="nav_selection",
        on_change=update_page
    )
    
    st.divider()
    
    total_books = len(st.session_state.library)
    read_books = sum(1 for book in st.session_state.library if book.get('read_status', False))
    
    if total_books > 0:
        read_percentage = (read_books / total_books) * 100
    else:
        read_percentage = 0
    
    st.markdown('<h3 class="section-header">Quick Stats</h3>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{total_books}</div>
            <div class="stat-label">Books</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{read_percentage:.1f}%</div>
            <div class="stat-label">Read</div>
        </div>
        """, unsafe_allow_html=True)
    
    if total_books > 0:
        unique_genres = set(book.get('genre', '') for book in st.session_state.library)
        st.markdown(f"<div class='stat-label'>Genres: {len(unique_genres)}</div>", unsafe_allow_html=True)

# Library page (unchanged)
if st.session_state.current_page == "Library":
    st.markdown('<h2 class="section-header">My Library</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        filter_options = ["All Books", "Read", "Unread"]
        unique_genres = list(set(book.get('genre', '') for book in st.session_state.library))
        filter_options.extend([f"Genre: {genre}" for genre in unique_genres if genre])
        
        st.session_state.filter_option = st.selectbox(
            "Filter by:",
            filter_options,
            index=filter_options.index(st.session_state.filter_option) if st.session_state.filter_option in filter_options else 0
        )
    
    with col2:
        sort_options = ["Title (A-Z)", "Title (Z-A)", "Author (A-Z)", "Author (Z-A)", "Year (Newest)", "Year (Oldest)"]
        st.session_state.sort_option = st.selectbox(
            "Sort by:",
            sort_options,
            index=sort_options.index(st.session_state.sort_option)
        )
    
    # Apply filters
    if st.session_state.filter_option == "All Books":
        filtered_library = st.session_state.library
    elif st.session_state.filter_option == "Read":
        filtered_library = [book for book in st.session_state.library if book.get('read_status', False)]
    elif st.session_state.filter_option == "Unread":
        filtered_library = [book for book in st.session_state.library if not book.get('read_status', False)]
    elif st.session_state.filter_option.startswith("Genre:"):
        genre = st.session_state.filter_option[7:]
        filtered_library = [book for book in st.session_state.library if book.get('genre', '') == genre]
    else:
        filtered_library = st.session_state.library
    
    # Apply sorting
    if st.session_state.sort_option == "Title (A-Z)":
        filtered_library = sorted(filtered_library, key=lambda x: x.get('title', '').lower())
    elif st.session_state.sort_option == "Title (Z-A)":
        filtered_library = sorted(filtered_library, key=lambda x: x.get('title', '').lower(), reverse=True)
    elif st.session_state.sort_option == "Author (A-Z)":
        filtered_library = sorted(filtered_library, key=lambda x: x.get('author', '').lower())
    elif st.session_state.sort_option == "Author (Z-A)":
        filtered_library = sorted(filtered_library, key=lambda x: x.get('author', '').lower(), reverse=True)
    elif st.session_state.sort_option == "Year (Newest)":
        filtered_library = sorted(filtered_library, key=lambda x: x.get('publication_year', 0), reverse=True)
    elif st.session_state.sort_option == "Year (Oldest)":
        filtered_library = sorted(filtered_library, key=lambda x: x.get('publication_year', 0))
    
    st.session_state.filtered_library = filtered_library
    
    if not filtered_library:
        st.info("No books found in your library. Add some books to get started!")
    else:
        for i, book in enumerate(filtered_library):
            display_book_card(book, i)

# Add Book page (unchanged)
elif st.session_state.current_page == "Add Book" or st.session_state.show_add_form:
    is_editing = st.session_state.edit_book is not None
    edit_book = st.session_state.edit_book if is_editing else None
    
    st.markdown(f'<h2 class="section-header">{"Edit Book" if is_editing else "Add New Book"}</h2>', unsafe_allow_html=True)
    
    with st.form("book_form"):
        title = st.text_input("Title", value=edit_book.get('title', '') if is_editing else '')
        author = st.text_input("Author", value=edit_book.get('author', '') if is_editing else '')
        
        col1, col2 = st.columns(2)
        with col1:
            year = st.number_input("Publication Year", min_value=1, max_value=datetime.now().year, 
                                  value=edit_book.get('publication_year', 2000) if is_editing else 2000)
        with col2:
            genre = st.text_input("Genre", value=edit_book.get('genre', '') if is_editing else '')
        
        read_status = st.checkbox("I have read this book", value=edit_book.get('read_status', False) if is_editing else False)
        
        if read_status:
            date_read = st.date_input("Date Read", 
                                     value=datetime.strptime(edit_book.get('date_read', datetime.now().strftime("%Y-%m-%d")), "%Y-%m-%d") if is_editing and edit_book.get('date_read') else datetime.now())
        else:
            date_read = None
        
        rating = st.slider("Rating (1-5)", min_value=1, max_value=5, 
                          value=edit_book.get('rating', 3) if is_editing and edit_book.get('rating') else 3)
        
        notes = st.text_area("Notes", value=edit_book.get('notes', '') if is_editing else '')
        
        submitted = st.form_submit_button("Save Book")
        
        if submitted:
            if not title:
                st.error("Title is required.")
            elif not author:
                st.error("Author is required.")
            else:
                book_data = {
                    'title': title.strip(),
                    'author': author.strip(),
                    'publication_year': year,
                    'genre': genre.strip(),
                    'read_status': read_status,
                    'rating': rating if read_status else None,
                    'notes': notes.strip(),
                }
                
                if read_status and date_read:
                    book_data['date_read'] = date_read.strftime("%Y-%m-%d")
                
                if is_editing:
                    for i, book in enumerate(st.session_state.library):
                        if book == edit_book:
                            st.session_state.library[i] = book_data
                            break
                    st.success(f"'{title}' has been updated in your library.")
                    st.session_state.edit_book = None
                    st.session_state.show_add_form = False
                    st.session_state.current_page = "Library"
                else:
                    st.session_state.library.append(book_data)
                    st.success(f"'{title}' has been added to your library.")
                    st.session_state.show_add_form = False
                    st.session_state.current_page = "Library"
                
                save_library(st.session_state.library)
                st.rerun()
    
    if is_editing:
        if st.button("Cancel Editing"):
            st.session_state.edit_book = None
            st.session_state.show_add_form = False
            st.session_state.current_page = "Library"
            st.rerun()

# Search Books page (unchanged)
elif st.session_state.current_page == "Search Books":
    st.markdown('<h2 class="section-header">Search Books</h2>', unsafe_allow_html=True)
    
    search_type = st.radio(
        "Search by:",
        ["Title", "Author", "Genre", "Year", "Advanced Search"]
    )
    
    if search_type == "Advanced Search":
        st.markdown("##### Use advanced search to find books with multiple criteria")
        col1, col2 = st.columns(2)
        
        with col1:
            title_query = st.text_input("Title contains:")
            author_query = st.text_input("Author contains:")
        
        with col2:
            genre_query = st.text_input("Genre contains:")
            year_query = st.number_input("Publication year:", min_value=0, max_value=datetime.now().year, value=0)
            
        read_status_query = st.radio("Read status:", ["Any", "Read Only", "Unread Only"])
        
        search_button = st.button("Search Library")
        
        if search_button:
            results = st.session_state.library.copy()
            
            if title_query:
                results = [book for book in results if title_query.lower() in book.get('title', '').lower()]
            if author_query:
                results = [book for book in results if author_query.lower() in book.get('author', '').lower()]
            if genre_query:
                results = [book for book in results if genre_query.lower() in book.get('genre', '').lower()]
            if year_query > 0:
                results = [book for book in results if book.get('publication_year', 0) == year_query]
            if read_status_query == "Read Only":
                results = [book for book in results if book.get('read_status', False)]
            elif read_status_query == "Unread Only":
                results = [book for book in results if not book.get('read_status', False)]
            
            if results:
                st.success(f"Found {len(results)} matching books.")
                for i, book in enumerate(results):
                    display_book_card(book, i, is_search=True)
            else:
                st.warning("No books found matching your criteria.")
    else:
        if search_type == "Title":
            query = st.text_input("Enter title to search for:")
            if query:
                results = [book for book in st.session_state.library if query.lower() in book.get('title', '').lower()]
        elif search_type == "Author":
            query = st.text_input("Enter author to search for:")
            if query:
                results = [book for book in st.session_state.library if query.lower() in book.get('author', '').lower()]
        elif search_type == "Genre":
            unique_genres = list(set(book.get('genre', '') for book in st.session_state.library if book.get('genre', '') != ''))
            if not unique_genres:
                st.info("No genres found in your library.")
                query = ""
                results = []
            else:
                query = st.selectbox("Select genre:", [""] + unique_genres)
                if query:
                    results = [book for book in st.session_state.library if book.get('genre', '') == query]
        elif search_type == "Year":
            query = st.number_input("Enter publication year:", min_value=0, max_value=datetime.now().year, value=0)
            if query > 0:
                results = [book for book in st.session_state.library if book.get('publication_year', 0) == query]
            else:
                results = []
        
        if 'query' in locals() and query:
            if results:
                st.success(f"Found {len(results)} matching books.")
                for i, book in enumerate(results):
                    display_book_card(book, i, is_search=True)
            else:
                st.warning("No books found matching your criteria.")

# Statistics page (unchanged)
elif st.session_state.current_page == "Statistics":
    st.markdown('<h2 class="section-header">Library Statistics</h2>', unsafe_allow_html=True)
    
    if not st.session_state.library:
        st.info("Add some books to your library to see statistics.")
    else:
        total_books = len(st.session_state.library)
        read_books = sum(1 for book in st.session_state.library if book.get('read_status', False))
        unread_books = total_books - read_books
        read_percentage = (read_books / total_books) * 100 if total_books > 0 else 0
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-number">{total_books}</div>
                <div class="stat-label">Total Books</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-number">{read_books}</div>
                <div class="stat-label">Read Books</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-number">{read_percentage:.1f}%</div>
                <div class="stat-label">Read Percentage</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        genre_counts = {}
        for book in st.session_state.library:
            genre = book.get('genre', 'Unknown')
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
        
        genre_df = pd.DataFrame({
            'Genre': list(genre_counts.keys()),
            'Count': list(genre_counts.values())
        }).sort_values('Count', ascending=False)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<h3 class="section-header">Books by Genre</h3>', unsafe_allow_html=True)
            fig = px.bar(genre_df, x='Genre', y='Count', color='Genre')
            fig.update_layout(
                xaxis_title="Genre",
                yaxis_title="Number of Books",
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown('<h3 class="section-header">Read vs Unread</h3>', unsafe_allow_html=True)
            pie_data = pd.DataFrame({
                'Status': ['Read', 'Unread'],
                'Count': [read_books, unread_books]
            })
            fig = px.pie(pie_data, values='Count', names='Status', color='Status',
                         color_discrete_map={'Read': '#10B981', 'Unread': '#F59E0B'})
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown('<h3 class="section-header">Books by Publication Year</h3>', unsafe_allow_html=True)
        
        year_counts = {}
        for book in st.session_state.library:
            year = book.get('publication_year', 'Unknown')
            if year != 'Unknown':
                year_counts[year] = year_counts.get(year, 0) + 1
        
        if year_counts:
            year_df = pd.DataFrame({
                'Year': list(year_counts.keys()),
                'Count': list(year_counts.values())
            }).sort_values('Year')
            
            fig = px.line(year_df, x='Year', y='Count', markers=True)
            fig.update_layout(
                xaxis_title="Publication Year",
                yaxis_title="Number of Books"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        rated_books = [book for book in st.session_state.library if book.get('rating') is not None]
        if rated_books:
            st.markdown('<h3 class="section-header">Top Rated Books</h3>', unsafe_allow_html=True)
            
            rated_books.sort(key=lambda x: x.get('rating', 0), reverse=True)
            top_rated = rated_books[:5]
            
            rating_df = pd.DataFrame({
                'Book': [f"{book.get('title', 'Unknown')} ({book.get('author', 'Unknown')})" for book in top_rated],
                'Rating': [book.get('rating', 0) for book in top_rated]
            })
            
            fig = px.bar(rating_df, x='Book', y='Rating', color='Rating',
                         color_continuous_scale='viridis')
            fig.update_layout(
                xaxis_title="",
                yaxis_title="Rating (1-5)",
                xaxis={'categoryorder':'total descending'}
            )
            st.plotly_chart(fig, use_container_width=True)

# Reading Challenge page (with fix)
elif st.session_state.current_page == "Reading Challenge":
    st.markdown('<h2 class="section-header">Reading Challenge</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #EFF6FF; border-radius: 10px; padding: 20px; margin-bottom: 20px;">
        <h3 style="color: #2563EB;">Set Your Reading Goal</h3>
        <p>Challenge yourself to read more books this year! Set a goal and track your progress.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        current_year = datetime.now().year
        books_read_this_year = sum(1 for book in st.session_state.library 
                                   if book.get('read_status', False) and 
                                   book.get('date_read', '').startswith(str(current_year)))
        
        st.session_state.reading_challenge = st.number_input(
            "Books to read this year:",
            min_value=1,
            value=st.session_state.reading_challenge if st.session_state.reading_challenge > 0 else 12
        )
        
        if st.button("Set Goal"):
            st.success(f"Goal set! You aim to read {st.session_state.reading_challenge} books this year.")
    
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{books_read_this_year}</div>
            <div class="stat-label">Books Read This Year</div>
        </div>
        """, unsafe_allow_html=True)
    
    if st.session_state.reading_challenge > 0:
        progress_percentage = min(100, (books_read_this_year / st.session_state.reading_challenge) * 100)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
        <h3 style="color: #2563EB;">Your Progress: {books_read_this_year} of {st.session_state.reading_challenge} books ({progress_percentage:.1f}%)</h3>
        """, unsafe_allow_html=True)
        
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = progress_percentage,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Reading Challenge Progress"},
            gauge = {
                'axis': {'range': [0, 100]},
                'bar': {'color': "#2563EB"},
                'steps': [
                    {'range': [0, 50], 'color': "#DBEAFE"},
                    {'range': [50, 80], 'color': "#93C5FD"},
                    {'range': [80, 100], 'color': "#60A5FA"}
                ]
            }
        ))
        
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
        
        books_with_dates = [book for book in st.session_state.library 
                           if book.get('read_status', False) and 
                           book.get('date_read', '').startswith(str(current_year))]
        
        if books_with_dates:
            books_with_dates.sort(key=lambda x: x.get('date_read', ''))
            
            st.markdown('<h3 class="section-header">Reading Timeline</h3>', unsafe_allow_html=True)
            
            date_df = pd.DataFrame({
                'Date': [book.get('date_read', '') for book in books_with_dates],
                'Book': [book.get('title', 'Unknown') for book in books_with_dates],
                'Author': [book.get('author', 'Unknown') for book in books_with_dates]
            })
            
            date_df['date_obj'] = pd.to_datetime(date_df['Date'])
            date_df['month'] = date_df['date_obj'].dt.strftime('%B')
            date_df['month_num'] = date_df['date_obj'].dt.month
            
            monthly_counts = date_df.groupby(['month', 'month_num']).size().reset_index(name='Count')
            monthly_counts = monthly_counts.sort_values('month_num')
            
            fig = px.bar(monthly_counts, x='month', y='Count', color='Count',
                         title=f"Books Read in {current_year} by Month")
            fig.update_layout(xaxis_title="Month",
                              yaxis_title="Books Read",
                              coloraxis_showscale=False)
            st.plotly_chart(fig, use_container_width=True)

            st.markdown('<h3 class="section-header">Books Read This Year</h3>', unsafe_allow_html=True)
            
            for book in books_with_dates:
                # Fix: Handle None rating by converting to 0 if None
                rating = book.get('rating', 0) if book.get('rating') is not None else 0
                st.markdown(f"""
                <div class="book-card">
                    <div class="book-title">{book.get('title', 'Unknown Title')}</div>
                    <div class="book-author">by {book.get('author', 'Unknown Author')}</div>
                    <div class="book-details">
                        Date Read: {book.get('date_read', 'Unknown')} | 
                        Rating: {'⭐' * rating}
                    </div>
                </div>
                """, unsafe_allow_html=True)

# Import/Export page (unchanged)
elif st.session_state.current_page == "Import/Export":
    st.markdown('<h2 class="section-header">Import/Export Library</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #EFF6FF; border-radius: 10px; padding: 20px; margin-bottom: 20px;">
        <h3 style="color: #2563EB;">Backup and Share Your Library</h3>
        <p>Export your library as a JSON file for backup or import a library from a JSON file.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Export Library")
        st.markdown("Download your current library as a JSON file.")
        
        if st.button("Export Library"):
            if not st.session_state.library:
                st.warning("Your library is empty. Nothing to export.")
            else:
                json_data = json.dumps(st.session_state.library, indent=4)
                st.download_button(
                    label="Download JSON",
                    data=json_data,
                    file_name="my_library.json",
                    mime="application/json"
                )
                st.success("Library ready for download.")
    
    with col2:
        st.markdown("### Import Library")
        st.markdown("Import a library from a JSON file.")
        
        uploaded_file = st.file_uploader("Choose a JSON file", type="json")
        
        if uploaded_file is not None:
            try:
                import_option = st.radio(
                    "Import option:",
                    ["Replace my current library", "Merge with my current library"]
                )
                
                if st.button("Import Library"):
                    imported_data = json.load(uploaded_file)
                    
                    if not isinstance(imported_data, list):
                        st.error("Invalid library format. Please upload a valid library JSON file.")
                    else:
                        if import_option == "Replace my current library":
                            st.session_state.library = imported_data
                            save_library(st.session_state.library)
                            st.success(f"Library replaced with {len(imported_data)} imported books.")
                            st.rerun()
                        else:
                            existing_titles = set((book.get('title', ''), book.get('author', '')) for book in st.session_state.library)
                            
                            new_books = []
                            for book in imported_data:
                                if (book.get('title', ''), book.get('author', '')) not in existing_titles:
                                    new_books.append(book)
                            
                            st.session_state.library.extend(new_books)
                            save_library(st.session_state.library)
                            st.success(f"Added {len(new_books)} new books to your library.")
                            st.rerun()
            except Exception as e:
                st.error(f"Error importing library: {e}")

if __name__ == "__main__":
    pass